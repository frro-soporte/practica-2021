"""Expresiones Booleanas."""

def es_vocal_if(letra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si letra es una vocal o
    no.

    Restricción: Utilizar un if para cada posibilidad con la función lower().
    Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods
    """
    if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u" or letra.lower() == "y":
        return True;
    else:
        False;
    pass # Completar

print("Detecta si hay un vocal en la frase: ", es_vocal_if("a"))
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
    if letra.lower() in "a" or letra.lower() in "e" or letra.lower() in "i" or letra.lower() in "o" or letra.lower() == "u" in letra.lower() == "y":
        return True
    else:
        False
    pass # Completar

print("Detecta si hay un vocal en la frase con in: ", es_vocal_if("a"))
# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    """Re-escribir utilizando el operador IN pero sin utilizar IF."""
    lista = ['a','e', 'i', 'o', 'u','y']
    return letra.lower() in lista
    pass # Completar


print("Detecta si hay un vocal en la frase con in sin if: ",es_vocal_in("a"))
# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
