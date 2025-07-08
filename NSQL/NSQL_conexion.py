from pymongo import MongoClient
from Auxiliares import Constantes

def get_coleccion(nombre_coleccion):
    """
    Conecta a la base de datos MongoDB y retorna la colección especificada.
    """
    cliente = MongoClient(Constantes.m_cliente)
    db = cliente[Constantes.DB]
    return db[nombre_coleccion]