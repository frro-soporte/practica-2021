"""Base de Datos SQL - Búsqueda"""

import datetime

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_01 import  cursor, conn


def buscar_persona(id_persona):

    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()

    consulta_sql = ''' SELECT IdPersona, Nombre, FechaNacimiento, DNI, Altura FROM persona WHERE IdPersona = ?'''
    cursor.execute(consulta_sql, (id_persona,))
    resultado = cursor.fetchone()

    conexion.close()

    if resultado:
        return resultado
    else:
        return False

    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    cursor.execute("SELECT * FROM Personas WHERE IdPersona = ?", (id_persona,))
    result = cursor.fetchone()
    print(result)
    if result is None:
        return False
    else:
        return result
    pass # Completar


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', '1988-05-15', 32165498, 180))
    assert juan == (1, 'juan perez', '1988-05-15', 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
