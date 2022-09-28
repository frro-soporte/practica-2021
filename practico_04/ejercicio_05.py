"""Base de Datos SQL - Modificación"""

import datetime
import sqlite3
from ejercicio_02 import agregar_persona
from ejercicio_01 import reset_tabla
from ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    """Implementar la funcion actualizar_persona, que actualiza un registro de
    una persona basado en su id. Devuelve un booleano en base a si encontro el
    registro y lo actualizo o no."""
    pass # Completar
    conn=sqlite3.connect('basededatos.db')
    cursor=conn.cursor()
    query=f"SELECT id_persona FROM persona WHERE id_persona={id_persona}"
    cursor.execute(query)
    if cursor.fetchone() is None:
        conn.commit()
        conn.close()
        return False
    else:   
        query2=f"UPDATE persona SET nombre='{nombre}', fecha_nacimiento='{nacimiento}', dni={dni}, altura={altura} WHERE id_persona={id_persona}"
        cursor.execute(query2)
        conn.commit()
        conn.close()
        return True

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', f"{datetime.datetime(1988, 4, 16)}", 32165497, 181)
    assert actualizar_persona(123, 'nadie', f"{datetime.datetime(1988, 4, 16)}", 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
