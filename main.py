from SQL import funciones_sql
from NSQL import funciones_NSQL

def menu_SQL():
    while True:
        print("""
--- Aguas Araucanía ---
1. Ver reclamos por cliente
2. Ver respuesta de reclamo
3. Ver todos los reclamos
4. Ver todos los clientes
0. salir
""")
        op = int(input('Ingrese una opción: '))
        if op == 1:
            nomcliente = input('Ingrese el nombre del cliente: ')
            funciones_sql.VerReclamosPorCliente(nomcliente)
        elif op == 2:
            idreclamo = input('Ingrese el id del reclamo: ')
            funciones_sql.VerRespuestaReclamo(idreclamo)
        elif op == 3:
            funciones_sql.VerTodosLosReclamos()
            op2= input('¿Desea exportar la lista de reclamos? (s/n): ')
            if op2 == 's':
                funciones_sql.ExportarReclamos()
                print('Lista de reclamos exportada exitosamente.') 
            elif op2 == 'n':
                print('No se exportó la lista de reclamos.')
            else:
                print('Opción no válida, no se exportó la lista de reclamos.')
        elif op == 4:
            funciones_sql.VerTodosLosClientes()
            op2 = input('¿Desea exportar la lista de clientes? (s/n): ')
            if op2 == 's':
                funciones_sql.ExportarClientes()
                print('Lista de clientes exportada exitosamente.')
            elif op2 == 'n':
                print('No se exportó la lista de clientes.')
            else:
                print('Opción no válida, no se exportó la lista de clientes.')
        elif op == 0:
            break
        else:
            print('Opción no válida')

def menu_Mongo():
    while True:
        print("""
--- Aguas Araucanía ---
1. Ver todas las encuestas.
2. Ver todos los comentarios.
3. Ver todos los archivos adjuntos.
4. Importar todos los clientes desde la db SQL.
0. Salir
""")
        op = int(input('Ingrese una opción: '))
        if op == 1:
            funciones_NSQL.VerTodasLasEncuestas()
        elif op == 2:
            funciones_NSQL.VerTodosLosComentarios()
        elif op == 3:
            funciones_NSQL.VerTodosLosArchivosAdjuntos()
        elif op == 4:
            funciones_NSQL.importarClientes()
            print('Clientes importados exitosamente.')
        elif op == 0:
            break
        else:
            print('Opción no válida')
            
def main_menu():
    while True:
        print("""
--- Aguas Araucanía ---
1. Ingresar a SQL
2. Ingresar a MongoDB
0. Salir""")
        op = int(input('Ingrese una opción: '))
        if op == 1:
            menu_SQL()
        elif op == 2:
            menu_Mongo()
        elif op == 0:
            print('Saliendo...')
            break
        else:
            print('Opción no válida')

if __name__ == "__main__":
    main_menu()