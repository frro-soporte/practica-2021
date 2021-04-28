"""Clousures, Generadores, Generadores Delegados

Esta guia muestra uno de los patrones avanzados de programación para evitar
el uso de variables globales. El método descripto se llama closure y consiste
en vincular una función con datos que persistan luego de la ejecución, sin
recurrir a variables globales. Esto se hace mediante la declaración de una
función dentro de otra y permite comportamiento que sería imposible lograr de
otra manera.
"""


from typing import Iterator, Callable


def generar_pares_clousure(initial: int = 0) -> Callable[[], int]:
    """Toma un número inicial y devuelve una función que cada vez que es
    invocada devuelve el número par siguiente al devuelto la última vez que
    fue invocada.

    Restricciones:
        - Usar closures
        - Usar el modificador nonlocal
    """
    def aux(nro: int = initial):
        nonlocal initial
        nro = initial
        if bool(nro % 2):
            initial += 1
            return initial
        initial += 2
        return nro
    return aux


# NO MODIFICAR - INICIO
generador_pares = generar_pares_clousure(0)
assert generador_pares() == 0
assert generador_pares() == 2
assert generador_pares() == 4
# NO MODIFICAR - FIN


###############################################################################


"""Este tipo de comportamiento es conocido com semi-corutina, las semi-corutinas
en Python son llamadas funciones generadoras y se caracterizan por utilizar el
yield en lugar del return.
"""


def generar_pares_generator(initial: int = 0) -> Iterator[int]:
    """Re-Escribir utilizando Generadores
    Referencia: https://docs.python.org/3/howto/functional.html?highlight=generator#generators
    """
    if initial % 2:  # si es impar lo mueve al proximo par
        initial += 1
    while True:
        yield initial  # interrumpe devolviendo valor y congelando func.
        initial += 2  # cuando retorna genera el sigiente par


# NO MODIFICAR - INICIO
generador_pares = generar_pares_generator()
assert next(generador_pares) == 0
assert next(generador_pares) == 2
assert next(generador_pares) == 4
# NO MODIFICAR - FIN


###############################################################################


def generar_pares_generator_send(initial: int = 0) -> Iterator[int]:
    """CHALLENGE OPCIONAL: Re-Escribir utilizando send para saltear numeros"""
    initial -= 2
    if initial % 2:
        initial += 1
    while True:
        initial += 2
        # se intrrumpe y luego val recibe los numeros enviados al momento de
        # continuar la func
        val = (yield initial)
        if val is not None:  # val recibe None si se retorna a la func con next() o con send(None)
            initial = val - 2  # cuando val no es None, recibe el proximo par a generar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    generador_pares = generar_pares_generator_send()
    assert next(generador_pares) == 0
    assert next(generador_pares) == 2
    assert next(generador_pares) == 4
    assert generador_pares.send(10) == 10
    assert next(generador_pares) == 12
    assert next(generador_pares) == 14
    assert next(generador_pares) == 16
# NO MODIFICAR - FIN


###############################################################################


# esta corrutina se encarga de E/S y correccion
def generar_pares_delegados(initial: int = 0) -> Iterator[int]:
    """CHALLENGE OPCIONAL: Re-Escribir utilizando Generadores delegados (yield from)"""
    while True:
        if initial % 2:
            initial += 1
        # delega en el generador los cambios de valor
        val = yield from sig_pares(initial)
        if val is not None:  # verifica si hay Entradas
            initial = val


# este generador se encarga de realizar incementos
def sig_pares(init: int) -> Iterator[int]:
    while True:
        yield init
        init += 2


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    generador_pares = generar_pares_delegados()
    assert next(generador_pares) == 0
    assert next(generador_pares) == 2
    assert next(generador_pares) == 4
# NO MODIFICAR - FIN
