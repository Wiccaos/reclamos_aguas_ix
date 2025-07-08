from . import NSQL_conexion
import csv, os
from SQL import funciones_sql

def VerTodasLasEncuestas():
    """Muestra todas las encuestas almacenadas en la colección de MongoDB."""
    try:
        coleccion = NSQL_conexion.get_coleccion('encuestas')  # Obtiene la colección de encuestas
        encuestas = coleccion.find()  # Recupera todos los documentos
        for encuesta in encuestas:
            # Imprime los datos relevantes de cada encuesta
            print(f"Reclamo ID: {encuesta.get('reclamo_id')}, Cliente ID: {encuesta.get('cliente_id')}, Fecha: {encuesta.get('fecha_respuesta')}, Puntuación: {encuesta.get('puntuacion')}, Comentario: {encuesta.get('comentario')}")
    except Exception as e:
        print(f"Error al obtener las encuestas: {e}")

def VerTodosLosComentarios():
    """Muestra todos los comentarios almacenados en la colección de MongoDB."""
    try:
        coleccion = NSQL_conexion.get_coleccion('comentarios_redes')  # Obtiene la colección de comentarios
        comentarios = coleccion.find()  # Recupera todos los documentos
        for comentario in comentarios:
            # Imprime los datos relevantes de cada comentario
            print(f"Plataforma: {comentario.get('plataforma')}, Usuario: {comentario.get('usuario')}, Fecha: {comentario.get('fecha')}, Contenido: {comentario.get('contenido')}")
    except Exception as e:
        print(f"Error al obtener los comentarios: {e}")

def VerTodosLosArchivosAdjuntos():
    """Muestra todos los archivos adjuntos almacenados en la colección de MongoDB."""
    try:
        coleccion = NSQL_conexion.get_coleccion('archivos_adjuntos')  # obtiene la colección de archivos adjuntos
        archivos = coleccion.find()  # Recupera todos los documentos
        for archivo in archivos:
            # Imprime los datos relevantes de cada archivo adjunto
            print(f"Reclamo ID: {archivo.get('reclamo_id')}, Tipo: {archivo.get('tipo_archivo')}, Nombre: {archivo.get('nombre_archivo')}, Ruta: {archivo.get('ruta_almacenamiento')}, Fecha subida: {archivo.get('fecha_subida')}")
    except Exception as e:
        print(f"Error al obtener los archivos adjuntos: {e}")

def importarClientes():
    """Importa los clientes desde un archivo CSV exportado por SQL a MongoDB."""
    funciones_sql.ExportarClientes()  # Exporta los clientes desde SQL a un archivo CSV
    try:
        # Construye la ruta al archivo CSV exportado
        ruta = os.path.join(os.path.dirname(__file__), '..', 'Auxiliares', 'clientes.csv')
        with open(ruta, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)  # Lee los datos del CSV como diccionarios
            datos = list(lector)
        if datos:
            coleccion = NSQL_conexion.get_coleccion('clientes')  # Obtiene la colección de clientes en MongoDB
            coleccion.insert_many(datos)  # Inserta todos los clientes en la colección
            print("Clientes importados correctamente.")
        else:
            print("No hay datos para importar.")
    except Exception as e:
        print(f"Error al importar clientes: {e}")

def importarReclamos():
    """Importa los reclamos desde un archivo CSV exportado por SQL a MongoDB."""
    funciones_sql.ExportarReclamos()  # Exporta los reclamos desde SQL a un archivo CSV
    try:
        # Construye la ruta al archivo CSV exportado
        ruta = os.path.join(os.path.dirname(__file__), '..', 'Auxiliares', 'reclamos.csv')
        with open(ruta, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)  # Lee los datos del CSV como diccionarios
            datos = list(lector)
        if datos:
            coleccion = NSQL_conexion.get_coleccion('reclamos')  # Obtiene la colección de reclamos en MongoDB
            coleccion.insert_many(datos)  # Inserta todos los reclamos en la colección
            print("Reclamos importados correctamente.")
        else:
            print("No hay datos para importar.")
    except Exception as e:
        print(f"Error al importar reclamos: {e}")

def importarRespuestas():
    """Importa las respuestas desde un archivo CSV exportado por SQL a MongoDB."""
    funciones_sql.ExportarRespuestas()  # Exporta las respuestas desde SQL a un archivo CSV
    try:
        # Construye la ruta al archivo CSV exportado
        ruta = os.path.join(os.path.dirname(__file__), '..', 'Auxiliares', 'respuestas.csv')
        with open(ruta, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)  # Lee los datos del CSV como diccionarios
            datos = list(lector)
        if datos:
            coleccion = NSQL_conexion.get_coleccion('respuestas')  # Obtiene la colección de respuestas en MongoDB
            coleccion.insert_many(datos)  # Inserta todas las respuestas en la colección
            print("Respuestas importadas correctamente.")
        else:
            print("No hay datos para importar.")
    except Exception as e:
        print(f"Error al importar respuestas: {e}")