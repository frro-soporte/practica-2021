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
    pass # Completar
    conn = sqlite3.connect('persona.db')
    c = conn.cursor()
    c.execute("""DROP TABLE IF EXISTS PERSONA""")
    c.execute("""CREATE TABLE PERSONA(IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,Nombre CHAR(30),FechaNacimiento DATE,DNI INTEGER,Altura INTEGER)""")
    conn.commit() 
    conn.close()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    pass # Completar
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute("""DROP TABLE IF EXISTS persona""")
    conn.commit()
    conn.close()
    


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
