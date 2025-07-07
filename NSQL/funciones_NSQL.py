from . import NSQL_conexion
import csv, os
from SQL import funciones_sql

def VerTodasLasEncuestas():
    try:
        coleccion = NSQL_conexion.colec_encuestas()
        encuestas = coleccion.find()
        for encuesta in encuestas:
            print(f"Reclamo ID: {encuesta.get('reclamo_id')}, Cliente ID: {encuesta.get('cliente_id')}, Fecha: {encuesta.get('fecha_respuesta')}, Puntuación: {encuesta.get('puntuacion')}, Comentario: {encuesta.get('comentario')}")
    except Exception as e:
        print(f"Error al obtener las encuestas: {e}")

def VerTodosLosComentarios():
    try:
        coleccion = NSQL_conexion.colec_comentarios()
        comentarios = coleccion.find()
        for comentario in comentarios:
            print(f"Plataforma: {comentario.get('plataforma')}, Usuario: {comentario.get('usuario')}, Fecha: {comentario.get('fecha')}, Contenido: {comentario.get('contenido')}")
    except Exception as e:
        print(f"Error al obtener los comentarios: {e}")

def VerTodosLosArchivosAdjuntos():
    try:
        from pymongo import MongoClient
        from Auxiliares import Constantes
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente[Constantes.DB]
        coleccion = db['archivos_adjuntos']
        archivos = coleccion.find()
        for archivo in archivos:
            print(f"Reclamo ID: {archivo.get('reclamo_id')}, Tipo: {archivo.get('tipo_archivo')}, Nombre: {archivo.get('nombre_archivo')}, Ruta: {archivo.get('ruta_almacenamiento')}, Fecha subida: {archivo.get('fecha_subida')}")
    except Exception as e:
        print(f"Error al obtener los archivos adjuntos: {e}")

def importarClientes():
    funciones_sql.ExportarClientes()
    try:
        ruta = os.path.join(os.path.dirname(__file__), '..', 'Auxiliares', 'clientes.csv')
        with open(ruta, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            datos = list(lector)
        if datos:
            coleccion = NSQL_conexion.colec_clientes()
            coleccion.insert_many(datos)
            print("Clientes importados correctamente.")
        else:
            print("No hay datos para importar.")
    except Exception as e:
        print(f"Error al importar clientes: {e}")

