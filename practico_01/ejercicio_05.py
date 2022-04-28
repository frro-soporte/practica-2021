"""Bucle FOR y Reduce."""

from typing import Iterable


def multiplicar_basico(numeros: Iterable[float]) -> float:
    """Toma un lista de números y devuelve el producto todos los númreos. Si
    la lista está vacia debe devolver 0.

    Restricciones: No usar bibliotecas auxiliares (Numpy, math, pandas).
    """
    pass  # Completar

    num = 1
    if numeros:
        for x in numeros:
            num = num * x
    else:
        num = 0
    return num
    

    """ Otra solucion 
    num = 1
    if len(numeros) == 0:
        return 0
    for x in numeros:
        num = num * x
    return num
      """




# NO MODIFICAR - INICIO
assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
assert multiplicar_basico(range(1, 20)) == 121_645_100_408_832_000
# NO MODIFICAR - FIN


###############################################################################


from functools import reduce


def multiplicar_reduce(numeros: Iterable[float]) -> float:
    """CHALLENGE OPCIONAL - Re-escribir utilizando reduce.
    Referencia: https://docs.python.org/3.8/library/functools.html#functools.reduce
    """ 
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert multiplicar_reduce([1, 2, 3, 4]) == 24
    assert multiplicar_reduce([2, 5]) == 10
    assert multiplicar_reduce([]) == 0
    assert multiplicar_reduce([1, 2, 3, 0, 4, 5]) == 0
    assert multiplicar_reduce(range(1, 20)) == 121_645_100_408_832_000
# NO MODIFICAR - FIN
