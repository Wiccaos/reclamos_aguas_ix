from SQL import funciones_sql
from NSQL import funciones_NSQL

def menu_SQL():
    """Menu para interactuar con la base de datos SQL."""
    while True:
        # Muestra las opciones disponibles para SQL
        print("""
--- Aguas Araucanía ---
1. Ver reclamos por cliente
2. Ver respuesta de reclamo
3. Ver todos los reclamos
4. Ver todos los clientes
5. ver todos las respuestas
0. salir
""")
        op = int(input('Ingrese una opción: '))
        if op == 1:
            # Solicita el nombre del cliente y muestra sus reclamos
            nomcliente = input('Ingrese el nombre del cliente: ')
            funciones_sql.VerReclamosPorCliente(nomcliente)
        elif op == 2:
            # Solicita el ID del reclamo y muestra su respuesta
            idreclamo = input('Ingrese el id del reclamo: ')
            funciones_sql.VerRespuestaReclamo(idreclamo)
        elif op == 3:
            # Muestra todos los reclamos y pregunta si desea exportarlos
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
            # Muestra todos los clientes y pregunta si desea exportarlos
            funciones_sql.VerTodosLosClientes()
            op2 = input('¿Desea exportar la lista de clientes? (s/n): ')
            if op2 == 's':
                funciones_sql.ExportarClientes()
                print('Lista de clientes exportada exitosamente.')
            elif op2 == 'n':
                print('No se exportó la lista de clientes.')
            else:
                print('Opción no válida, no se exportó la lista de clientes.')
        elif op == 5:
            # Muestra todas las respuestas y pregunta si desea exportarlas
            funciones_sql.verTodasLasRespuestas()
            op2 = input('¿Desea exportar la lista de respuestas? (s/n): ')
            if op2 == 's':
                funciones_sql.exportarRespuestas()
                print('Lista de respuestas exportada exitosamente.')
            elif op2 == 'n':
                print('No se exportó la lista de respuestas.')
            else:
                print('Opción no válida, no se exportó la lista de respuestas.')
        elif op == 0:
            # Sale del menú SQL
            break
        else:
            print('Opción no válida')

def menu_Mongo():
    """Menu para interactuar con la base de datos MongoDB."""
    while True:
        # Muestra las opciones disponibles para MongoDB
        print("""
--- Aguas Araucanía ---
1. Ver todas las encuestas.
2. Ver todos los comentarios.
3. Ver todos los archivos adjuntos.
4. Importar todos los clientes desde la db SQL.
5. importar todos los reclamos desde la db SQL.
6. importar todas las respuestas desde la db SQL.
0. Salir
""")
        op = int(input('Ingrese una opción: '))
        if op == 1:
            # Muestra todas las encuestas almacenadas en MongoDB
            funciones_NSQL.VerTodasLasEncuestas()
        elif op == 2:
            # Muestra todos los comentarios almacenados en MongoDB
            funciones_NSQL.VerTodosLosComentarios()
        elif op == 3:
            # Muestra todos los archivos adjuntos almacenados en MongoDB
            funciones_NSQL.VerTodosLosArchivosAdjuntos()
        elif op == 4:
            # Importa todos los clientes desde la base de datos SQL a MongoDB
            funciones_NSQL.importarClientes()
            print('Clientes importados exitosamente.')
        elif op == 5:
            # Importa todos los reclamos desde la base de datos SQL a MongoDB
            funciones_NSQL.importarReclamos()
            print('Reclamos importados exitosamente.')
        elif op == 6:
            # Importa todas las respuestas desde la base de datos SQL a MongoDB
            funciones_NSQL.importarRespuestas()
            print('Respuestas importadas exitosamente.')
        elif op == 0:
            # Sale del menú MongoDB
            break
        else:
            print('Opción no válida')
            
def main_menu():
    """Menu principal para seleccionar entre SQL y MongoDB."""
    while True:
        # Muestra el menú principal para elegir el tipo de base de datos
        print("""
--- Aguas Araucanía ---
1. Ingresar a SQL
2. Ingresar a MongoDB
0. Salir""")
        op = int(input('Ingrese una opción: '))
        if op == 1:
            # Ingresa al menú de SQL
            menu_SQL()
        elif op == 2:
            # Ingresa al menú de MongoDB
            menu_Mongo()
        elif op == 0:
            # Sale del programa
            print('Saliendo...')
            break
        else:
            print('Opción no válida')

if __name__ == "__main__":
    # Inicia el menú principal solo si el archivo se ejecuta directamente
    main_menu()