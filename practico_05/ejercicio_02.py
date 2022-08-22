"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_05.ejercicio_01 import Base, Socio

from typing import List, Optional

engine = create_engine('sqlite:///socios.db?check_same_thread=False')
Base.metadata.bind = engine
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()


class DatosSocio():

    def __init__(self):
        pass # Completar

    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        pass # Completar
        socio = session.query(Socio).filter(Socio.id == id_socio).first()
        if socio is None:
            return None
        return socio


    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        pass # Completar
        socio = session.query(Socio).filter(Socio.dni == dni_socio).first()
        if socio is None:
            return None
        return socio
        
    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        pass # Completar
        return session.query(Socio).all()

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        pass # Completar
        session.query(Socio).delete()
        session.commit()
        socios = session.query(Socio).all()
        if socios is None:
            return True
        return False


    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        pass # Completar
        nuevo_socio = socio
        session.add(nuevo_socio)
        session.commit()
        return nuevo_socio

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        pass # Completar
        session.query(Socio).filter(Socio.id == id_socio).delete()
        session.commit()
        socio_borrado = session.query(Socio).get(id_socio)
        if socio_borrado is None:
            return True
        return False

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        pass # Completar
        socio_db = session.query(Socio).filter(Socio.id == socio.id).first()
        socio_db.nombre = socio.nombre
        socio_db.apellido = socio.apellido
        socio_db.dni = socio.dni
        session.add(socio_db)
        session.commit()
        return socio_db

    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        pass # Completar
        return session.query(Socio).count()


# NO MODIFICAR - INICIO

# Test Creación
datos = DatosSocio()

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
assert socio.id > 0

# Test Baja
assert datos.baja(socio.id) == True

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id) == socio_2

# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2

# Test Modificación
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id)
assert socio_3_modificado.id == socio_3.id
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587

# Test Conteo
assert len(datos.todos()) == 3

# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0

# NO MODIFICAR - FIN