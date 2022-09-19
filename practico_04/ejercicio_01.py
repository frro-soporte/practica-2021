"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    conexion=sqlite3.connect("ejercicio12dointento.db")
    try:
        conexion.execute("""create table Persona (
                              IdPersona integer primary key autoincrement,
                              Nombre varchar(30),
                              FechaNacimiento date,
                              DNI integer,
                              Altura integer
                        )""")
        print("se creo la tabla Persona")
    except sqlite3.OperationalError:
        print("La tabla Persona ya existe")                    
        conexion.close()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    conexion=sqlite3.connect("ejercicio12dointento.sql")
    try:
        conexion.execute("""drop table if exists Persona
                        """)
        print("se borro la tabla Persona")                        
    except sqlite3.OperationalError:
        print("No anduvo")                    
        conexion.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN

crear_tabla()
borrar_tabla()