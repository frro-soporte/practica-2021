"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio
from sqlalchemy.exc import IntegrityError
from typing import List, Optional

class DatosSocio():

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        pass # Completar

    def buscar(self, id_socio: int) -> Optional[Socio]:
        socio = self.session.query(Socio).filter_by(id=id_socio).first()
        if socio is not None:
            return socio
        else:
            return None
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        pass # Completar

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        socio = self.session.query(Socio).filter_by(dni=dni_socio).first()
        if socio is not None:
            return socio
        else:
            return None
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        pass # Completar
        
    def todos(self) -> List[Socio]:
        ls = self.session.query(Socio).all()
        print('Lista de Socios:')
        for s in ls:
            print('Socio:', s.id, s.dni, s.nombre, s.apellido)
        return ls
        """Devuelve listado de todos los socios en la base de datos."""
        pass # Completar

    def borrar_todos(self) -> bool:
        try:
            self.session.query(Socio).delete()
            self.session.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar todos los datos: {str(e)}")
            self.session.rollback()
            return False

        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        pass # Completar

    def alta(self, socio: Socio) -> Socio:
      try:
          self.session.add(socio)
          self.session.commit()
          return socio
      except IntegrityError:
          self.session.rollback()
          print("El DNI del socio ya existe en la base de datos.")
          return None
          """Agrega un nuevo socio a la tabla y lo devuelve"""
      pass # Completar

    def baja(self, id_socio: int) -> bool:
        socio = self.session.query(Socio).filter_by(id=id_socio).first()
        if socio is not None:
            self.session.delete(socio)
            self.session.commit()
            return True
        else:
            return False
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        pass # Completar

    def modificacion(self, socio: Socio) -> Socio:
        self.session.merge(socio)
        self.session.commit()
        return socio
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        pass # Completar
    
    def contarSocios(self) -> int:
        return self.session.query(Socio).count()
        """Devuelve el total de socios que existen en la tabla"""
        pass # Completar



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
