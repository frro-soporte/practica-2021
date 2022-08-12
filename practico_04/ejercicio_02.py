"""Base de Datos SQL - Alta"""

import datetime
#from practico_04.ejercicio_01 import reset_tabla
#Este from no nos funciona desde la carpeta raíz. De la manera que lo hicimos funcionar es pararse dentro de la carpeta practico_04 y escribirlo como:
from ejercicio_01 import reset_tabla
import sqlite3

def agregar_persona(nombre, nacimiento, dni, altura):
    """Implementar la funcion agregar_persona, que inserte un registro en la 
    tabla Persona y devuelva los datos ingresados el id del nuevo registro."""
    pass # Completar
    conn = sqlite3.connect('persona.db')
    c = conn.cursor()
    c.execute("INSERT INTO persona(Nombre,FechaNacimiento,DNI,Altura) VALUES (?, ?, ?, ?)", (nombre, nacimiento, dni, altura))
    conn.commit()
    conn.close()
    return c.lastrowid

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
