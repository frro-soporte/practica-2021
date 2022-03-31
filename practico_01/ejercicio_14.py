"""Apply, Partial

En múltiples librerías se estila tener una función llamada apply que aplica
una función a todos los elementos de un conjunto de datos, puede ser una
tabla en una base de datos, una columna en un DataFrame o una fila en un
arreglo multidimensional. El problema suele estar en que esta función apply
sólo admite funciones de ún parámetro. Para poder superar esta dificultad,
debe hacerse uso de la función partial.
"""

from functools import partial
from typing import Callable, Iterable


def apply(lista: Iterable[int], func: Callable[[int], bool]) -> Iterable[bool]:
    """Toma una lista y una función que toma un parámetro y devuelve una lista
    con la función aplicada a todos los elementos."""
    resp=[]
    for i in lista:
        resp.append(func(i))
    return resp
    


# NO MODIFICAR - INICIO
def esta_entre_valores(x: int, min_: float, max_: float) -> bool:
    return min_ < x < max_
# NO MODIFICAR - FIN
valores=[10,20,30,40,50,200,400,1234]
esta_entre_valores.apply(valores, esta_entre_valores)
###############################################################################


"""Utilizar partial para que pueda pasarse como parámetro a la función apply
Referencia: https://docs.python.org/3/library/functools.html#functools.partial
"""

lista = [3, 4, 5, 6, 7, 8]
min_ = 4
max_ = 7
nueva_funcion = # Completar

# NO MODIFICAR - INICIO
lista = [3, 4, 5, 6, 7, 8]
assert [False, False, True, True, False, False] == apply(lista, nueva_funcion)
# NO MODIFICAR - FIN
