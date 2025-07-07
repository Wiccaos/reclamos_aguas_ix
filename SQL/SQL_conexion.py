import mysql.connector
from Auxiliares import Constantes

def SQLconexion():
    """Establece una conexión con la base de datos MySQL."""
    try:
        # Intenta establecer la conexión usando los parámetros definidos en Constantes
        cnx_sql = mysql.connector.connect(
            host= Constantes.HOST,
            user= Constantes.USER,
            password= Constantes.PASSWORD,
            database= Constantes.DB,
            port= Constantes.PORT_SQL
        )
        print("Conexion con MySQL establecida correctamente")
        return cnx_sql  # Devuelve el objeto de conexión si fue exitosa
    except mysql.connector.Error as e:
        # Captura y muestra cualquier error de conexión
        print(f"Error al conectar a MySQL: {e}")
        return None  # Devuelve None si la conexión falla
