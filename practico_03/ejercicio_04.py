"""Herencia"""


# NO MODIFICAR - INICIO
class Animal:
    def __init__(self, edad: int = 0):
        self.edad = edad

    def descripcion(self) -> str:
        return f"Tengo {self.edad} años"
# NO MODIFICAR - FIN


class Perro(Animal):
    """Escribir un constructor que añada una variable de instancia llamada raza,
    de tipo string y que tenga como valor por defecto "". Adicionalmente se debe
    sobrecargar el método descripción para que devuelva:
    "Soy un perro y" + método descripción del padre
    """
    def __init__(self, edad: int = 0,raza = ""):
        super().__init__(edad)
        self.raza = raza

    def descripcion(self) -> str:
        return f"Soy un perro y {super().descripcion()}"
    # Completar


# NO MODIFICAR - INICIO
terrier = Perro(edad=8, raza="Yorkshire Terrier")
cachorro = Perro(edad=1)
dogo = Perro(raza="Dogo")

assert Animal(10).descripcion() == "Tengo 10 años"
assert terrier.descripcion() == "Soy un perro y Tengo 8 años"
assert dogo.descripcion() == "Soy un perro y Tengo 0 años"
assert cachorro.descripcion() == "Soy un perro y Tengo 1 años"
# NO MODIFICAR - FIN


"""Re-Escribir utilizando DataClasses"""

from dataclasses import dataclass


@dataclass
class Animal:
    edad : int = 0

    def descripcion(self) -> str:
        return f"Tengo {self.edad} años"
    pass # Completar


@dataclass
class Perro(Animal):
    raza : str = ""

    def descripcion(self) -> str:
        return f"Soy un perro y {super().descripcion()}"
    pass # Completar


# NO MODIFICAR - INICIO
terrier = Perro(edad=8, raza="Yorkshire Terrier")
cachorro = Perro(edad=1)
dogo = Perro(raza="Dogo")

assert Animal(10).descripcion() == "Tengo 10 años"
assert terrier.descripcion() == "Soy un perro y Tengo 8 años"
assert dogo.descripcion() == "Soy un perro y Tengo 0 años"
assert cachorro.descripcion() == "Soy un perro y Tengo 1 años"
# NO MODIFICAR - FIN
