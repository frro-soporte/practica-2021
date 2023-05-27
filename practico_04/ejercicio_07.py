"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime

from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_06 import reset_tabla
from practico_04.ejercicio_01 import cursor, conn
from practico_04.ejercicio_04 import buscar_persona


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
    search = buscar_persona(id_persona)
    if not search:
        print("La persona buscada no esta encontrado")
        return False
    else:
        cursor.execute("SELECT * FROM PersonaPesos WHERE IdPersona = ? AND Fecha > ?", (id_persona, fecha))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO PersonaPesos(IdPersona,Fecha,Peso) VALUES(?,?,?)",(id_persona, fecha, peso))
            return cursor.lastrowid
        else:
            return False
    pass # Completar


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
