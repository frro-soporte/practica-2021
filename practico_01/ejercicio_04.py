"""Expresiones Booleanas."""


from doctest import ELLIPSIS_MARKER


def es_vocal_if(letra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si letra es una vocal o
    no.

    Restricción: Utilizar un if para cada posibilidad con la función lower().
    Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods
    """
    l = letra.lower()
    if l == 'a':
        return True
    elif l == 'e':
        return True
    elif l == 'i':
        return True
    elif l == 'o':
        return True
    elif l == 'u':
        return True
    else:
        return False


# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    """Re-escribir utilizando un sólo IF y el operador IN.
    Referencia: https://docs.python.org/3/reference/expressions.html#membership-test-operations
    """
    vocales = ['a','e','i','o','u','A','E','I','O','U']
    if letra in vocales:
        return True
    else:
        return False



# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    """Re-escribir utilizando el operador IN pero sin utilizar IF."""
    vocales = ['a','e','i','o','u','A','E','I','O','U']
    return letra in vocales


# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
