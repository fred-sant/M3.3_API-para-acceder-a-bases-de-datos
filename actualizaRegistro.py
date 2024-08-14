from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'user': 'u927419088_admin',
    'password': '#Admin12345#',
    'host': '195.179.238.58',
    'database': 'u927419088_testing_sql'
}

# Función para conectar a la base de datos
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Ruta para obtener todos los registros de la tabla Curso
@app.route('/cursos', methods=['GET'])
def get_cursos():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM curso')
    cursos = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(cursos)

# Ruta para obtener un registro específico de la tabla Curso
@app.route('/curso/<int:curso_id>', methods=['GET'])
def get_curso(curso_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM curso WHERE idCurso = %s', (curso_id,))
    curso = cursor.fetchone()
    cursor.close()
    connection.close()

    if curso is None:
        return jsonify({'error': 'Registro no encontrado'}), 404

    return jsonify(curso)

# Ruta para actualizar un registro específico de la tabla Curso
@app.route('/curso/update/<int:curso_id>', methods=['GET'])
def update_curso(curso_id):
    nombre = request.args.get('nombreDescriptivo')
    nAsignaturas = request.args.get('nAsignaturas')

    if not nombre or not nAsignaturas:
        return jsonify({'error': 'Faltan parámetros'}), 400

    connection = get_db_connection()
    cursor = connection.cursor()
    update_query = '''
    UPDATE curso
    SET nombreDescriptivo = %s, nAsignaturas = %s
    WHERE idCurso = %s
    '''
    cursor.execute(update_query, (nombre, nAsignaturas, curso_id))
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({'message': 'Registro actualizado exitosamente'})

if __name__ == '__main__':
    app.run(debug=True)
