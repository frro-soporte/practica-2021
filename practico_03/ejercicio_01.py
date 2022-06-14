"""Constructor, Variables de instancia y métodos de instacia"""

from typing import Optional


class Rectangulo:
    """
    Implementar la clase Rectangulo que contiene una base y una altura, y el
    método area.
    """
    # Completar
    def __init__(self, base: float = None, altura: float = None) -> None:
        self.base : float = base
        self.altura : float = altura
        
    def area(self) -> float:
        if self.base != None and self.altura != None:
            return self.base * self.altura
        else:
            return 0

# NO MODIFICAR - INICIO

# Test Constructor
rec = Rectangulo(10, 10)
assert rec.base == 10
assert rec.altura == 10
assert rec.area() == 100

# Test Valores por defecto
rec = Rectangulo()
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
