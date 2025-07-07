from pymongo import MongoClient
from Auxiliares import Constantes

def get_coleccion(nombre_coleccion):
    """
    Conecta a la base de datos MongoDB y retorna la colección especificada.
    """
    # Crea un cliente de MongoDB usando la URL definida en Constantes
    cliente = MongoClient(Constantes.m_cliente)
    # Selecciona la base de datos definida en Constantes
    db = cliente[Constantes.DB]
    # Retorna la colección solicitada
    return db[nombre_coleccion]

# Funciones para obtener cada colección específica de la base de datos

def colec_clientes():
    """Retorna la colección 'clientes'"""
    return get_coleccion('clientes')

def colec_encuestas():
    """Retorna la colección 'encuestas'"""
    return get_coleccion('encuestas')

def colec_comentarios():
    """Retorna la colección 'comentarios_redes'"""
    return get_coleccion('comentarios_redes')

def colec_archivos_adjuntos():
    """Retorna la colección 'archivos_adjuntos'"""
    return get_coleccion('archivos_adjuntos')

