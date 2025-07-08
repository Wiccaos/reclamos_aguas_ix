from pymongo import MongoClient
import pandas as pd
import mysql.connector
from Auxiliares import Constantes
from NSQL import NSQL_conexion
import os

def obtener_tabla_mysql(query):
    """Ejecuta un query en MySQL y retorna un DataFrame."""
    cnx = mysql.connector.connect(
        host=Constantes.HOST,
        user=Constantes.USER,
        password=Constantes.PASSWORD,
        database=Constantes.DB,
        port=Constantes.PORT_SQL
    )
    cursor = cnx.cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)
    cursor.close()
    cnx.close()
    return df

def obtener_datos_mysql():
    """Obtiene clientes, reclamos y respuestas desde MySQL."""
    clientes = obtener_tabla_mysql("SELECT * FROM clientes")
    reclamos = obtener_tabla_mysql("SELECT * FROM reclamos")
    respuestas = obtener_tabla_mysql("SELECT * FROM respuestas")
    return clientes, reclamos, respuestas

def obtener_datos_mongo():
    """Obtiene encuestas de satisfacción y comentarios de redes desde MongoDB."""
    encuestas = list(NSQL_conexion.get_coleccion('encuestas_satisfaccion').find())
    comentarios = list(NSQL_conexion.get_coleccion('comentarios_redes').find())
    # Limpia el campo _id de MongoDB
    for doc in encuestas + comentarios:
        doc.pop('_id', None)
    df_encuestas = pd.DataFrame(encuestas)
    df_comentarios = pd.DataFrame(comentarios)
    return df_encuestas, df_comentarios

def consolidar_y_exportar():
    # Obtiene datos de ambas fuentes
    clientes, reclamos, respuestas = obtener_datos_mysql()
    encuestas, comentarios = obtener_datos_mongo()

    # Une reclamos con clientes y respuestas
    reclamos_full = reclamos.merge(clientes, on='id_cliente', suffixes=('', '_cliente'))
    reclamos_full = reclamos_full.merge(respuestas, left_on='id_reclamo', right_on='reclamo_id', how='left', suffixes=('', '_respuesta'))

    # Une encuestas de satisfacción por id_reclamo
    if not encuestas.empty:
        reclamos_full = reclamos_full.merge(
            encuestas[['reclamo_id', 'puntuacion', 'comentario']],
            left_on='id_reclamo',
            right_on='reclamo_id',
            how='left',
            suffixes=('', '_encuesta')
        )

    # Exporta a Excel y CSV en la carpeta Reportes
    os.makedirs('Reportes', exist_ok=True)
    reclamos_full.to_excel(os.path.join('Reportes', 'reporte_consolidado.xlsx'), index=False)
    reclamos_full.to_csv(os.path.join('Reportes', 'reporte_consolidado.csv'), index=False)
    print("Reporte consolidado generado: Reportes/reporte_consolidado.xlsx y Reportes/reporte_consolidado.csv")

if __name__ == "__main__":
    consolidar_y_exportar()
