"""Propiedades"""


class Auto:
    """La clase auto tiene dos propiedades, precio y marca. La marca se define
    obligatoriamente al construir la clase y siempre que se devuelve, se 
    devuelve con la primer letra en mayúscula y no se puede modificar. El precio
    puede modificarse pero cuando se muestra, se redondea a 2 decimales
    
    Restricción: Usar Properties
    
    Referencia: https://docs.python.org/3/library/functions.html#property"""

    def __init__(self, marca, precio=0):
        self._marca = marca
        self._precio = precio
    
    def getPrecio(self):
        return round(self._precio, 2)
    
    def setPrecio(self, precio):
        self._precio = precio
    
    precio = property(getPrecio, setPrecio)

    @property
    def nombre(self):
        return self._marca.capitalize()


# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)

assert auto.nombre == "Ford"
assert auto.precio == 12_875.46
auto.precio = 13_874.349
assert auto.precio == 13_874.35

try:
    auto.nombre = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass
import string
from sys import flags

@dataclass#(frozen=True)
class Auto:
    """Re-Escribir utilizando DataClasses"""
    
    nombre: string
    precio: float
    flag: bool = True

    """
    def precio(self):
        return round(self.precio, 2)

    def precio(self, p):
        object.__setattr__(self, "precio", p)
    """

    def getPrecio(self):
        return round(self.precio, 2)
    
    def setPrecio(self, precio):
        #object.__setattr__(self, "precio", precio)
        self.precio=precio
    


# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)
print("ok1")
assert auto.nombre == "Ford"
print("ok2")
assert auto.precio == 12_875.46
auto.precio = 13_874.349
print("ok3")
assert auto.precio == 13_874.35
print("ok4")
try:
    auto.nombre = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN
print("ok5")