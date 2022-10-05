"""Bucle FOR y Reduce."""

from typing import Iterable, Sized


def multiplicar_basico(numeros: Iterable[float]) -> float:
    """Toma un lista de números y devuelve el producto todos los números. Si
    la lista está vacia debe devolver 0.

    Restricciones: No usar bibliotecas auxiliares (Numpy, math, pandas).
    """
    total=1
    cant=0
    for num in numeros:
        total=num*total
        cant=cant+1
    if cant!=0:
        return total
    return cant

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
    return reduce(lambda a, b: a*b, numeros, 1 if len(list(numeros))!=0 else float(0))

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert multiplicar_reduce([1, 2, 3, 4]) == 24
    assert multiplicar_reduce([2, 5]) == 10
    assert multiplicar_reduce([]) == 0
    assert multiplicar_reduce([1, 2, 3, 0, 4, 5]) == 0
    assert multiplicar_reduce(range(1, 20)) == 121_645_100_408_832_000
# NO MODIFICAR - FIN
