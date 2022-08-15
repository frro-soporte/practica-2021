"""Base de Datos SQL - Baja"""

import datetime
import sqlite3
from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    pass # Completar

    conn = sqlite3.connect('persona.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM persona WHERE IdPersona=?", (id_persona, ))
    count = c.fetchall()[0][0]
    c.execute("DELETE FROM persona WHERE IdPersona=?", (id_persona, ))
    conn.commit()
    conn.close()

    if count == 0:
        return False
    else: 
        return True

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
