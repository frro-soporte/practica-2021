"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

"""Declaraciones global"""
conn = sqlite3.connect("pracrica_04_ejercicio_01.db")
"""Permitir de realizar varios aciones"""
cursor = conn.cursor()

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - integer: Int()
    """
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS Personas (
                                  IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
                                  Nombre CHAR(30) NOT NULL,
                                  FechaNacimiento DATETIME NOT NULL,
                                  DNI INTEGER NOT NULL,
                                  integer INTEGER NOT NULL
                            )""")
        """print("se creo la tabla Personas")"""
    except sqlite3.OperationalError:
        print("La tabla Personas ya existe")
    conn.commit()
    #conn.close()
    pass # Completar


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    try:
        cursor.execute("""DROP TABLE  Personas""")
        print("se elimino la tabla Personas")
    except sqlite3.OperationalError:
        print("La tabla Personas ya no existe")
    conn.commit()
    conn.close()
    pass # Completar
"""borrar_tabla()"""
# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
