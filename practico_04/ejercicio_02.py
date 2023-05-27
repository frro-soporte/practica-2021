"""Base de Datos SQL - Alta"""

import datetime
from practico_04.ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    
    conexion = sqlite3.connect('mi_base_de_datos.db')

    cursor = conexion.cursor()

    comando_sql = '''INSERT INTO persona (Nombre, FechaNacimiento, DNI, Altura) 
    VALUES (?, ?, ?, ?)'''

    valores = (nombre, nacimiento, dni, altura)
    cursor.execute(comando_sql, valores)

    id_nuevo = cursor.lastrowid

    conexion.commit()
    conexion.close()

    return id_nuevo
    """Implementar la funcion agregar_persona, que inserte un registro en la 
    tabla Persona y devuelva los datos ingresados el id del nuevo registro."""
    pass # Completar



# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', '1988-05-15', 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', '1980-01-25', 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
