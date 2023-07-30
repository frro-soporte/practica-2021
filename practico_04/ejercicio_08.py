"""Base de datos SQL - Listar"""

import datetime

from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_06 import reset_tabla
from practico_04.ejercicio_07 import agregar_peso
from practico_04.ejercicio_01 import cursor, conn
from practico_04.ejercicio_04 import buscar_persona


def listar_pesos(id_persona):

    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()

    persona = buscar_persona(id_persona)
    if not persona:
        conexion.close()
        return False

    consulta_sql = '''SELECT Fecha, Peso FROM PersonaPeso WHERE IdPersona = ?'''
    cursor.execute(consulta_sql, (id_persona,))
    resultado = cursor.fetchall()
    conexion.close()
    if resultado is None:
        return False
    return [(str(fecha), peso) for fecha, peso in resultado]

    """Implementar la funcion listar_pesos, que devuelva el historial de pesos 
    para una persona dada.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
     mplementadas).

    Debe devolver:
    - Lista de (fecha, peso), donde fecha esta representado por el siguiente 
    formato: AAAA-MM-DD.

    Ejemplo:
    [
        ('2018-01-01', 80),
        ('2018-02-01', 85),
        ('2018-03-01', 87),
        ('2018-04-01', 84),
        ('2018-05-01', 82),
    ]

    - False en caso de no cumplir con alguna validacion.
    """

    search = buscar_persona(id_persona)
    if not search:
        print("La persona buscada no esta encontrado")
        return False
    else:
        cursor.execute("SELECT Fecha, Peso FROM PersonaPesos WHERE IdPersona = ? ", (id_persona, ))
        result = cursor.fetchall()

        """
            Es 10 de la fecha, significa toma los 10 primeros caratecteres de la fecha
            para no mostrar la hora (2018-01-01) 
        """
        result = [(Fecha[:10], Peso) for Fecha, Peso in result]

        if result is not None:
            return result
        else:
            return False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez','1988-05-15', 32165498, 180)
    agregar_peso(id_juan, '2018-05-01', 80)
    agregar_peso(id_juan, '2018-06-01', 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
