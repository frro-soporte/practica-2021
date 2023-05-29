"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime

from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()

    persona = buscar_persona(id_persona)
    if not persona:
        conexion.close()
        return False

    consulta_sql = '''SELECT Fecha FROM PersonaPeso WHERE IdPersona = ? AND Fecha > ?'''
    cursor.execute(consulta_sql, (id_persona, fecha))
    registros = cursor.fetchall()
    if registros:
        conexion.close()
        return False

    comando_sql = '''INSERT INTO PersonaPeso (IdPersona, Fecha, Peso) VALUES (?, ?, ?)'''
    values = (id_persona, fecha, peso)
    cursor.execute(comando_sql, values)
    conexion.commit()
    id_peso = cursor.lastrowid
    conexion.close()
    return id_peso

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

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', '1988-05-15', 32165498, 180)
    assert agregar_peso(id_juan, '2018-05-26', 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, '1988-05-15', 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, '2018-05-16', 80) == False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
