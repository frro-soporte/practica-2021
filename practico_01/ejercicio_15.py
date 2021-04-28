"""Higher Order Functions, Decoradores, Memoized

Python permite funciones de orden superior, es decir, funciones que toman
otras funciones como parámetros. Esto posibilita una serie de patrones que
en otros lenguajes son difíciles de implementar y hace sencilla la
implementación de patrones como el decorador.


Caso de uso 1: Medir el tiempo de las funciones

En Python existe la función perf_counter del módulo time de la biblioteca
estandar que permite medir el tiempo con cierta precisión entre invocaciones.

Para poder utilizar un ejemplo real, se utilizará una función que calcula
y cuenta las permutaciones (una operación costosa computacionalmente).
"""

from functools import partial
from itertools import permutations
from time import perf_counter
from typing import Callable, Sequence, Tuple


# NO MODIFICAR - INICIO
def calcular_posibilidades(lista: Sequence[int], limite: int) -> int:
    count = 0
    for i in range(limite):
        for _ in permutations(lista, i):
            count += 1
    return count


n = 11
limite = 10
lista = list(range(n))

start = perf_counter()
result = calcular_posibilidades(lista, limite)
elapsed = perf_counter() - start

print(f"Tiempo: {elapsed:2.2f} segundos - Enfoque procedural")
assert result == 28671512
# NO MODIFICAR - FIN


###############################################################################


def medir_tiempo(func: Callable[[], int]) -> Tuple[int, float]:
    """Toma una función y devuelve una dupla conteniendo en su primer elemento
    el resultado de la función y en su segundo elemento el tiempo de ejecución.

    Restricción: La función no debe tomar parámetros y por lo tanto se
    recomienda usar partial.
    """
    start = perf_counter()  # toma tiempo como punto de partida
    resultado = func()  # como entra con partial solo hay que llamarla para que la ejecute
    # toma tiempo como punto final y le resta el punto de partida
    stop = perf_counter() - start
    return resultado, stop


# NO MODIFICAR - INICIO
result, elapsed = medir_tiempo(partial(calcular_posibilidades, lista, limite))
print(f"Tiempo: {elapsed:2.2f} segundos - Usando Partial")
assert result == 28671512
# NO MODIFICAR - FIN


###############################################################################


def medir_tiempo(func: Callable[[Sequence[int], int], int]
                 ) -> Callable[[Sequence[int], int], Tuple[int, float]]:
    """Re-Escribir utilizando closures de forma tal que la función no requiera
    partial. En este caso se debe devolver una función que devuelva la tupla y
    tome una cantidad arbitraria de parámetros.
    """

    def aplica_func(
            parametros: Sequence[int] = lista, detencion: int = limite) -> Tuple[int, float]:
        inicio: float = perf_counter()
        # func es parametro en el closure
        resultado = func(parametros, detencion)
        fin: float = perf_counter() - inicio  # inicio esta definido en el closure
        return resultado, fin

    # devuelve una funcion que espera parametros para aplicar otra
    # funcion[func]
    return aplica_func


# NO MODIFICAR - INICIO
calcular_posibilidades_nueva = medir_tiempo(calcular_posibilidades)
result, elapsed = calcular_posibilidades_nueva(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Decorador")
assert result == 28671512
# NO MODIFICAR - FIN


###############################################################################


"""La función anterior cumple con las condiciones necesarias para ser utilizada
como decorador en Python. Utilizar la sintaxis especial de decoradores (el @)
y re-definir la función calcular_posibilidades con esta nueva sintaxis.

Referencia: https://docs.python.org/3/glossary.html#term-decorator

Este es un ejemplo y no hay que escribir código.
"""


# NO MODIFICAR - INICIO
@medir_tiempo
def calcular_posibilidades(lista: Sequence[int], limite: int) -> int:
    count = 0
    for i in range(limite):
        for _ in permutations(lista, i):
            count += 1
    return count


result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Decorador con sintaxis especial")
assert result == 28671512
# NO MODIFICAR - FIN


###############################################################################


"""Un caso real de este patrón es guardar en una memoria cache auxiliar
resultados de funciones que son muy costosas computacionalmente. A este
patrón se lo suele denominar memoized
"""


def memoized(func):
    """Escribir una función memoized y utilizarla como decorador junto con medir_
    tiempo para la función calcular posibilidades. Prestar atención a los tiempo
    de ejecución
    """
    try:
        len(ejecutadas)  # Verifica existencia de diccionario de funciones
    except NameError:
        ejecutadas = dict()  # Crea diccionario en caso de no existir
    finally:
        if func in ejecutadas:
            # busca el resultado si la funcion ya fue ejecutada
            return ejecutadas[func]
        else:
            resultado = func  # ejecuta si la funcion no ha sido ejecutada aun
            # almacena resultado de la ejecucion
            ejecutadas.update({func: resultado})
        return resultado


@medir_tiempo
@memoized
def calcular_posibilidades(lista: Sequence[int], limite: int) -> int:
    count = 0
    for i in range(limite):
        for _ in permutations(lista, i):
            count += 1
    return count


# NO MODIFICAR - INICIO
print()

result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Con Memoized - 1ra ejecución")
assert result == 28671512

result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.8f} segundos - Con Memoized - 2da ejecución")
assert result == 28671512

result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.8f} segundos - Con Memoized - 3ra ejecución")
assert result == 28671512
# NO MODIFICAR - FIN


###############################################################################


"""CHALLENGE OPCIONAL: Esta es otra ocasión donde las funciones recursivas
tienen ventajas adicionales  ya que al utilizar el patrón memoized, las
funciones recursivas permiten ejecuciones más rápidas para las llamadas
sucesivas.
"""


@medir_tiempo
@memoized
def calcular_posibilidades_recursiva(lista: Sequence[int], limite: int) -> int:
    """Re-Escribir de manera recursiva"""
    limite -= 1

    def cuenta(lista: Sequence[int], limite: int):
        if limite == 0:
            return 1
        cont = 0
        for _ in permutations(lista, limite):
            cont += 1
        cont = cont + cuenta(lista, limite - 1)
        return cont
    return cuenta(lista, limite)


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    print()

    result, elapsed = calcular_posibilidades_recursiva(lista, limite)
    print(
        f"Tiempo: {elapsed:2.2f} segundos - Recursiva Memoized - 1ra Ejecución")
    print(result)
    assert result == 28671512

    result, elapsed = calcular_posibilidades_recursiva(lista, limite)
    print(
        f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - 2da Ejecución")
    assert result == 28671512

    print()

    result, elapsed = calcular_posibilidades(lista, limite + 1)
    print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro + 1")
    assert result == 68588312

    result, elapsed = calcular_posibilidades_recursiva(lista, limite + 1)
    print(
        f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro + 1")
    assert result == 68588312

    print()

    result, elapsed = calcular_posibilidades(lista, limite + 2)
    print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro + 2")
    assert result == 108505112

    result, elapsed = calcular_posibilidades_recursiva(lista, limite + 2)
    print(
        f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro + 2")
    assert result == 108505112

    print()

    result, elapsed = calcular_posibilidades(lista, limite - 1)
    print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro - 1")
    assert result == 8713112

    result, elapsed = calcular_posibilidades_recursiva(lista, limite - 1)
    print(
        f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro - 1")
    assert result == 8713112

    print()

    result, elapsed = calcular_posibilidades(lista, limite - 2)
    print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro - 2")
    assert result == 2060312

    result, elapsed = calcular_posibilidades_recursiva(lista, limite - 2)
    print(
        f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro - 2")
    assert result == 2060312
# NO MODIFICAR - FIN
