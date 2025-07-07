from pymongo import MongoClient
from Auxiliares import Constantes

def colec_clientes():
    """
    Conecta a la base de datos MongoDB y retorna la colección de clientes.
    """
    cliente=MongoClient("mongodb://localhost:27017/")
    db = cliente[Constantes.DB]
    coleccion_clientes = db['clientes']
    return coleccion_clientes

def colec_encuestas():
    """
    Conecta a la base de datos MongoDB y retorna la colección de encuestas.
    """
    cliente=MongoClient("mongodb://localhost:27017/")
    db = cliente[Constantes.DB]
    coleccion_encuestas = db['encuestas']
    return coleccion_encuestas

def colec_comentarios():
    """
    Conecta a la base de datos MongoDB y retorna la colección de comentarios de redes.
    """
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente[Constantes.DB]
    coleccion_comentarios = db['comentarios_redes']  # Cambiado aquí
    return coleccion_comentarios
