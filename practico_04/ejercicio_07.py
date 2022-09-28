"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime
import sqlite3

from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""

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
        query2=f"SELECT fecha FROM personapeso WHERE id_persona={id_persona} AND fecha > '{fecha}'"
        cursor.execute(query2)
        if cursor.fetchone() is None:
            query3=f"INSERT INTO personapeso (id_persona, fecha, peso) VALUES ({id_persona},'{fecha}',{peso})"
            cursor.execute(query3)
            query4=f"SELECT peso FROM personapeso WHERE id_persona={id_persona} AND fecha='{fecha}'"
            cursor.execute(query4)
            devid=cursor.fetchone()[0]
            conn.commit()
            conn.close()
            return devid
        else:
            conn.commit()
            conn.close()
            return False



# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
