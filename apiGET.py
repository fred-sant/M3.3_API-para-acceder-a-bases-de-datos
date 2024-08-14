from flask import Flask, jsonify
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

# Ruta para obtener los registros de la tabla Curso
@app.route('/cursos', methods=['GET'])
def get_cursos():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM curso')
    cursos = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(cursos)

if __name__ == '__main__':
    app.run(debug=True)
