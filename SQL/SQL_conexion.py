import mysql.connector
from Auxiliares import Constantes

def SQLconexion():
    try:
        cnx_sql = mysql.connector.connect(
            host= Constantes.HOST,
            user= Constantes.USER,
            password= Constantes.PASSWORD,
            database= Constantes.DB,
            port= Constantes.PORT_SQL
        )
        print("Conexion con MySQL establecida correctamente")
        return cnx_sql
    except mysql.connector.Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None
