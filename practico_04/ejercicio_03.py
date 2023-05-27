"""Base de Datos SQL - Baja"""

import datetime

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_01 import cursor, conn


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""

    #Consulta si existe esa persona con ese id
    cursor.execute("SELECT * FROM Personas WHERE IdPersona = ?", (id_persona, ))
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        cursor.execute("DELETE FROM Personas WHERE IdPersona = ?", (id_persona, ))
        conn.commit()
        return True
    pass # Completar

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
