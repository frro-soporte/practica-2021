"""Any y Sets."""

from typing import Any, Iterable


def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Toma dos listas y devuelve un booleano en base a si tienen al menos 1
    elemento en común.
    Restricción: Utilizar bucles anidados.
    """
    common = set(lista_1).intersection(lista_2)
    if len(common):
        return True
    else:
        return False
    pass # Completar


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
print("Superposicion de dos lista: ",superposicion_basico(test_list, (2, "world", 35.20)))
assert superposicion_basico(test_list, (2, "world", 35.20))
assert not superposicion_basico(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_in(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando un sólo bucle y el operador IN."""

    common = [x for x in lista_1 if x in lista_2]
    if len(common):
        return True
    else:
        return False

    pass # Completar


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
print("Superposicion de dos lista con in: ",superposicion_basico(test_list, (2, "world", 35.20)))
assert superposicion_in(test_list, (2, "world", 35.20))
assert not superposicion_in(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando sin bucles, el operador in y la funcion any.
    Referencia: https://docs.python.org/3/library/functions.html#any
    """
    return any(x for x in lista_1 if x in lista_2)
    pass # Completar


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
print("Superposicion de dos lista con any: ",superposicion_any(test_list, (2, "world", 35.20)))
assert superposicion_any(test_list, (2, "world", 35.20))
assert not superposicion_any(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando conjuntos (sets).
    Referencia: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
    """
    common = set(lista_1) & set(lista_2)
    if len(common):
        return True
    else:
        return False
    pass # Completar


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
print("Superposicion de dos lista con set: ",superposicion_set(test_list, (2, "world", 35.20)))
assert superposicion_set(test_list, (2, "world", 35.20))
assert not superposicion_set(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN
