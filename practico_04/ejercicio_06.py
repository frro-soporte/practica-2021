def crear_tabla_peso():
    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='PersonaPeso'")
    tabla_existente = cursor.fetchone()

    if tabla_existente is not None:
        print("La tabla ya existe")
    else:
        consulta_sql = '''CREATE TABLE PersonaPeso (
            IdPersona INTEGER,
            Fecha TEXT,
            Peso INTEGER,
            FOREIGN KEY (IdPersona) REFERENCES persona(IdPersona)
        )'''

        cursor.execute(consulta_sql)

        conexion.commit()
        conexion.close()
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """

    pass # Completar


def borrar_tabla_peso():
    conexion = sqlite3.connect('mi_base_de_datos.db')
    cursor = conexion.cursor()

    comando_sql = '''DROP TABLE IF EXISTS PersonaPeso'''

    cursor.execute(comando_sql)

    conexion.commit()
    conexion.close()


    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    pass # Completar


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
