import os, csv
from . import SQL_conexion
from prettytable import from_db_cursor

def VerReclamosPorCliente(nomcliente):
    cnx_sql = SQL_conexion.SQLconexion()
    if cnx_sql is None:
        print("No se pudo conectar a la base de datos.")
        return
    cursor = cnx_sql.cursor()
    try:
        consulta = """
        SELECT 
            r.id_reclamo AS reclamo_id,
            c.nombre AS cliente_nombre,
            c.correo AS cliente_correo,
            r.fecha_creacion,
            r.titulo,
            r.descripcion
        FROM aguas_araucania.reclamos r
        JOIN aguas_araucania.clientes c ON r.id_cliente = c.id_cliente
        WHERE c.nombre LIKE %s;
        """
        cursor.execute(consulta, (f"%{nomcliente}%",))
        tab = from_db_cursor(cursor)
        print(tab)
    except Exception as e:
        print(f"\nNo hay resultados o error: {e}\n")
    finally:
        cursor.close()
        cnx_sql.close()

def VerRespuestaReclamo(idreclamo):
    cnx_sql = SQL_conexion.SQLconexion()
    if cnx_sql is None:
        print("No se pudo conectar a la base de datos.")
        return
    cursor = cnx_sql.cursor()
    try:
        consulta = """
        SELECT 
            r.titulo AS titulo_reclamo,
            r.descripcion AS descripcion_reclamo,
            r.fecha_creacion,
            c.nombre AS cliente_nombre,
            c.correo AS cliente_correo,
            resp.fecha AS fecha_respuesta,
            resp.contenido AS contenido_respuesta,
            s.nombre AS soporte_nombre
        FROM aguas_araucania.reclamos r
        JOIN aguas_araucania.clientes c ON r.id_cliente = c.id_cliente
        LEFT JOIN aguas_araucania.respuestas resp ON r.id_reclamo = resp.reclamo_id
        LEFT JOIN aguas_araucania.soporte s ON resp.soporte_id = s.id_sup
        WHERE r.id_reclamo = %s
        ORDER BY resp.fecha ASC;
        """
        cursor.execute(consulta, (idreclamo,))
        tab = from_db_cursor(cursor)
        print(tab)
    except Exception as e:
        print(f"\nNo hay resultados o error: {e}\n")
    finally:
        cursor.close()
        cnx_sql.close()

def VerTodosLosClientes():
    cnx_sql = SQL_conexion.SQLconexion()
    if cnx_sql is None:
        print("No se pudo conectar a la base de datos.")
        return 
    cursor = cnx_sql.cursor()
    try:
        consulta = "SELECT * FROM aguas_araucania.clientes;"
        cursor.execute(consulta)
        tab = from_db_cursor(cursor)
        print(tab)
    except Exception as e:
        print(f"\nNo hay resultados o error: {e}\n")
    finally:
        cursor.close()
        cnx_sql.close()

def ExportarClientes():
    cnx_sql = SQL_conexion.SQLconexion()
    if cnx_sql is None:
        print("No se pudo conectar a la base de datos.")
        return
    cursor = cnx_sql.cursor()
    try:
        consulta = "SELECT * FROM aguas_araucania.clientes;"
        cursor.execute(consulta)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        # Asegura que la carpeta Auxiliares existe
        ruta = os.path.join(os.path.dirname(__file__), '..', 'Auxiliares', 'clientes.csv')
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(rows)
        print("Lista de clientes exportada exitosamente en Auxiliares/clientes.csv.")
    except Exception as e:
        print(f"Error al exportar la lista de clientes: {e}")
    finally:
        cursor.close()
        cnx_sql.close()

def VerTodosLosReclamos():
    cnx_sql = SQL_conexion.SQLconexion()
    if cnx_sql is None:
        print("No se pudo conectar a la base de datos.")
        return 
    cursor = cnx_sql.cursor()
    try:
        consulta = "SELECT * FROM aguas_araucania.reclamos;"
        cursor.execute(consulta)
        tab = from_db_cursor(cursor)
        print(tab)
    except Exception as e:
        print(f"\nNo hay resultados o error: {e}\n")
    finally:
        cursor.close()
        cnx_sql.close()

def ExportarReclamos():
    cnx_sql = SQL_conexion.SQLconexion()
    if cnx_sql is None:
        print("No se pudo conectar a la base de datos.")
        return
    cursor = cnx_sql.cursor()
    try:
        consulta = "SELECT * FROM aguas_araucania.reclamos;"
        cursor.execute(consulta)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        # Asegura que la carpeta Auxiliares existe
        ruta = os.path.join(os.path.dirname(__file__), '..', 'Auxiliares', 'reclamos.csv')
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(rows)
        print("Lista de reclamos exportada exitosamente en Auxiliares/reclamos.csv.")
    except Exception as e:
        print(f"Error al exportar la lista de reclamos: {e}")
    finally:
        cursor.close()
        cnx_sql.close()