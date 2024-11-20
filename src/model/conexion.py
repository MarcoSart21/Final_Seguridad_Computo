import pyodbc

# Especifica los detalles de la conexión
server = 'localhost\\SQLEXPRESS'
database = 'seguridad'
username = 'sa'
password = 'skul'

# Construye la cadena de conexión
conexion = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'UID=' + username + ';'
    'PWD=' + password + ';'
)

# Intenta establecer la conexión
try:
    conexion = pyodbc.connect(conexion)
    print("Conexión exitosa a SQL Server")
    
except pyodbc.Error as e:
    print("Error al conectar a SQL Server:", e)