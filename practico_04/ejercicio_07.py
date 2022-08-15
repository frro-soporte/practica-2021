"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime
import sqlite3
from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_06 import reset_tabla
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

    pass # Completar

    persona = buscar_persona(id_persona)

    conn = sqlite3.connect('personapeso.db')
    c = conn.cursor()
    c.execute("SELECT IdPersona, MAX(Fecha), Peso FROM personapeso WHERE IdPersona=? GROUP BY IdPersona", (id_persona,))
    persona_peso = c.fetchone()
    if persona_peso is not None:
        persona_peso_list = list(persona_peso)
        persona_peso_list[1] = datetime.datetime.strptime(persona_peso[1][0:10], '%Y-%m-%d')
        persona_fecha = persona_peso_list[1]

    if not persona:
        return False
    else:
        if not persona_peso:
            c.execute("INSERT INTO personapeso(IdPersona, Fecha, Peso) VALUES (?, ?, ?)", (id_persona, fecha, peso))
            conn.commit()
            conn.close()
            return c.lastrowid
        elif fecha <= persona_fecha:
            return False
        else:
            c.execute("INSERT INTO personapeso(IdPersona, Fecha, Peso) VALUES (?, ?, ?)", (id_persona, fecha, peso))
            conn.commit()
            conn.close()
            return c.lastrowid



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
