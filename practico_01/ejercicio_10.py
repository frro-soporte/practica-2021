"""For-Else, Any."""

from typing import Iterable


def tiene_pares_basico(numeros: Iterable[int]) -> bool:
    """Toma una lista y devuelve un booleano en función si tiene al menos un
    número par."""
    pass # Completar
    valor = False
    for x in numeros:
        if x % 2 == 0:
            valor = True

    return valor


# NO MODIFICAR - INICIO
assert tiene_pares_basico([1, 3, 5]) is False
assert tiene_pares_basico([1, 3, 5, 6]) is True
assert tiene_pares_basico([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN


###############################################################################

from typing import Iterable


def tiene_pares_for_else(numeros: Iterable[int]) -> bool:
    """Re-Escribir utilizando for-else con dos return y un break.
    Referencia: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
    """
    pass # Completar
    for x in numeros:
        if x % 2 == 0:
            return True
    else:
        return False
    

# NO MODIFICAR - INICIO
assert tiene_pares_for_else([1, 3, 5]) is False
assert tiene_pares_for_else([1, 3, 5, 6]) is True
assert tiene_pares_for_else([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN


###############################################################################


def tiene_pares_any(numeros: Iterable[int]) -> bool:
    """Re-Escribir utilizando la función any, sin utilizar bucles.
    Referencia: https://docs.python.org/3/library/functions.html#any
    """
    return(any(x % 2 == 0 for x in numeros))

# NO MODIFICAR - INICIO
assert tiene_pares_any([1, 3, 5]) is False
assert tiene_pares_any([1, 3, 5, 6]) is True
assert tiene_pares_any([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN
