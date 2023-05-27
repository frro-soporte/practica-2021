"""Base de Datos SQL - Creación de tablas auxiliares"""

from practico_04.ejercicio_01 import borrar_tabla, crear_tabla
from practico_04.ejercicio_01 import cursor, conn


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    cursor.execute("""CREATE TABLE IF NOT EXISTS PersonaPesos (
               Id INTEGER PRIMARY KEY AUTOINCREMENT,
               IdPersona INTEGER NOT NULL,
               Fecha DATE NOT NULL,
               Peso INTEGER NOT NULL,
               FOREIGN KEY(IdPersona) REFERENCES persona(Id)
               )""")
    conn.commit()
    print("Tabla PersonaPesos fue creada con exito")
    pass # Completar


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    conn.execute("DROP TABLE IF EXISTS personaPeso")
    conn.commit()
    print("Tabla PersonaPesos fue borrada con exito")
    pass # Completar

#Para probar la creacion y la eliminacion
#crear_tabla_peso()
#borrar_tabla_peso()
# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
