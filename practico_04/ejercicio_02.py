"""Base de Datos SQL - Alta"""

import datetime
from ejercicio_01 import reset_tabla
import sqlite3

def agregar_persona(nombre, nacimiento, dni, altura):
    """Implementar la funcion agregar_persona, que inserte un registro en la 
    tabla Persona y devuelva los datos ingresados el id del nuevo registro."""
    pass # Completar
    reset_tabla(agregar_persona)
    conn=sqlite3.connect('basededatos.db')
    cursor=conn.cursor()
    query=f"INSERT INTO persona (nombre, fecha_nacimiento, dni, altura) VALUES ('{nombre}',{nacimiento},{dni},{altura})"
    cursor.execute(query)
    query2=f"SELECT id_persona FROM persona WHERE dni={dni}"
    devdni=cursor.execute(query2)
    print(devdni)
    conn.commit()
    conn.close()
    return devdni

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
