"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():

    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='persona'")
    tabla_existente = cursor.fetchone()

    if tabla_existente is not None:
      print("La tabla ya existe")
    else:
      creacion_persona = '''CREATE TABLE persona (
        IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT,
        FechaNacimiento TEXT,
        DNI INTEGER,
        Altura INTEGER
       )'''
    
      cursor.execute(creacion_persona)

      conexion.commit()
      conexion.close()
      pass # Completar



def borrar_tabla():
    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()

    comando_sql = '''DROP TABLE IF EXISTS persona'''

    cursor.execute(comando_sql)

    conexion.commit()
    conexion.close()


    pass # Completar


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
