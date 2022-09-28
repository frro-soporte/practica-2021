"""Base de Datos SQL - Baja"""

import datetime

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona
import sqlite3

def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
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
        query2=f"DELETE FROM persona WHERE id_persona={id_persona}"
        cursor.execute(query2)
        conn.commit()
        conn.close()
        return True
    
    
# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
