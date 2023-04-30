"""Constructor, Variables de instancia y métodos de instacia"""

from typing import Optional


class Rectangulo:
    """
    Implementar la clase Rectangulo que contiene una base y una altura, y el
    método area.
    """

    def __init__(self, base = None, altura = None):
        self.base = base
        self.altura = altura

    def area(self):
        if self.base is None:
            pass
        if self.altura is None:
            pass
        if self.altura is None and self.base is None:
            return 0
        return self.base * self.altura

    # Completar


# NO MODIFICAR - INICIO

# Test Constructor
rec = Rectangulo(10, 10)

print("base del rectángulo: ", rec.base)
print("altura del rectángulo: ", rec.altura)
print("Área del rectángulo: ", rec.area())
print()

assert rec.base == 10
assert rec.altura == 10
assert rec.area() == 100

# Test Valores por defecto
rec = Rectangulo()

print("base del rectángulo is None: ", rec.base)
print("altura del rectángulo is None: ", rec.altura)
print("Área del rectángulo == 0: ", rec.area())
print()

assert rec.base is None
assert rec.altura is None
assert rec.area() == 0

rec.base = 10
rec.altura = 10

assert rec.base == 10
assert rec.altura == 10
assert rec.area() == 100

# Test Instanciación sin variable
assert Rectangulo(10, 10).area() == 100
assert Rectangulo(10, 0).area() == 0
assert Rectangulo(0, 10).area() == 0
# NO MODIFICAR - FIN
