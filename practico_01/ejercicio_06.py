"""Type, Comprensión de Listas, Sorted y Filter."""

#from curses.ascii import isdigit
from typing import List, Union

from sympy import numer, true


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    pass # Completar
    numeros=[]
    cadenas=[]
    todojunto=[]
    for elemento in lista:
        if type(elemento)==int:
            numeros.append(elemento)
        else:
            cadenas.append(elemento)
    todojunto.extend(cadenas)
    todojunto.extend(numeros)
    return todojunto

# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""
    pass # Completar
    numeros=[]
    cadenas=[]
    todojunto=[]
    numeros=[elemento for elemento in lista if type(elemento)==int]
    cadenas=[elemento for elemento in lista if type(elemento)!=int]
    todojunto.extend(cadenas)
    todojunto.extend(numeros)
    return todojunto

# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    pass # Completar
    lista = sorted(lista, key=lambda x: type(x) in (int,float))
    return lista

# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    todojunto=[]
    numeros = list(filter(lambda x: type(x)==int,lista))
    cadenas = list(filter(lambda x: type(x)!=int,lista))
    todojunto.extend(cadenas)
    todojunto.extend(numeros)
    return todojunto


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    pass # Completar
    str(lista)
    nros = []
    letras = []
    for x in lista:
        if type(x) in (int, float):
            nros.append(x)
        elif type(x) == str:
            letras.append(x)
    return letras + nros

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
