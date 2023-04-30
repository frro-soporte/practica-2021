"""Herencia"""


# NO MODIFICAR - INICIO
class Animal:
    def __init__(self, edad: int = 0, raza: str = ""):
        self.raza = raza
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
    def descripcion(self) -> str:
        return f"Soy un perro y {Animal.descripcion(self).lower()}"
    # Completar


# NO MODIFICAR - INICIO
terrier = Perro(edad=8, raza="Yorkshire Terrier")
cachorro = Perro(edad=1)
dogo = Perro(raza="Dogo")

print("Perro terrier: ",terrier.descripcion())
print("Perro cachorro: ", cachorro.descripcion())
print("Perro dogo: ", dogo.descripcion())
print("")

assert Animal(10).descripcion() == "Tengo 10 años"
assert terrier.descripcion() == "Soy un perro y tengo 8 años"
assert dogo.descripcion() == "Soy un perro y tengo 0 años"
assert cachorro.descripcion() == "Soy un perro y tengo 1 años"
# NO MODIFICAR - FIN


"""Re-Escribir utilizando DataClasses"""

from dataclasses import dataclass


@dataclass
class Animal:
    edad: int = 0
    raza: str = ""
    def descripcion(self) -> str:
        return f"Tengo {self.edad} años"
    pass # Completar

@dataclass
class Perro(Animal):

    def descripcion(self) -> str:
        return f"Soy un perro y {Animal.descripcion(self).lower()}"
    pass # Completar


# NO MODIFICAR - INICIO
terrier = Perro(edad=8, raza="Yorkshire Terrier")
cachorro = Perro(edad=1)
dogo = Perro(raza="Dogo")

print("Perro terrier with @dataclass: ",terrier.descripcion())
print("Perro cachorro with @dataclass: ", cachorro.descripcion())
print("Perro dog with @dataclasso: ", dogo.descripcion())
print("Animal(10).descripcion(): " ,Animal(10).descripcion())
print("")

assert Animal(10).descripcion() == "Tengo 10 años"
assert terrier.descripcion() == "Soy un perro y tengo 8 años"
assert dogo.descripcion() == "Soy un perro y tengo 0 años"
assert cachorro.descripcion() == "Soy un perro y tengo 1 años"
# NO MODIFICAR - FIN
