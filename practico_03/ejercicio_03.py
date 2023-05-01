"""Dataclasses"""


class Persona:
    """Clase con los siguientes miembros:

    Atributos de instancia:
    - nombre: str
    - edad: int
    - sexo (H hombre, M mujer): str
    - peso: float
    - altura: float

    Métodos:
    - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
    """

    def __init__(self, nombre: str,edad: int, sexo: str,peso: float, altura: float):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return  False


    # Completar
ismayor = Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad()
if ismayor:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")
# NO MODIFICAR - INICIO
assert Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad()
assert not Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad()
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int
    sexo: str
    peso: float
    altura: float
    """Re-Escribir utilizando DataClasses"""

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
    # Completar

ismayor = Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad()
if ismayor:
    print("Es mayor de edad with @dataclass")
else:
    print("No es mayor de edad with @dataclass")
# NO MODIFICAR - INICIO
assert Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad()
assert not Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad()
# NO MODIFICAR - FIN
