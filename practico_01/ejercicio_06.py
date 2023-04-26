"""Type, Comprensión de Listas, Sorted y Filter."""
import string
from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    listint = []
    liststring = []
    if len(lista) == 0:
        return 0
    for i in lista:
        if type(i) == int:
            listint.append(i)
        else:
            liststring.append(i)
    return (liststring + listint)
    pass # Completar


print("numeros al final basico: ",numeros_al_final_basico([3, "a", 1, "b", 10, "j"]))
# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""
    listint = []
    liststring = []
    if len(lista) == 0:
        return 0

    #lista2 = [elemento for elemento in lista if type(elemento) == int]
    #print("Lista compre: ",lista2)

    for i in lista:
        if type(i) == int:
            listint.append(i)
        else:
            liststring.append(i.title().lower())
    return (liststring + listint)
    pass # Completar


print("numeros al final basico con comprension: ",numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]))
# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    listint = []
    liststring = []
    if len(lista) == 0:
        return 0
    for i in lista:
        if type(i) == int:
            listint.append(i)
        else:
            liststring.append(i)
    return (sorted(liststring) + listint)
    pass # Completar


print("numeros al final basico con sorted: ",numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]))
# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    list_int = (x for x in lista if type(x) == int)
    list_str = (x for x in lista if type(x) == string)
    return (sorted(list_str, key = None, reverse=False) + sorted(list_int, key = None, reverse = False))
    pass # Completar


print("numeros al final by filer: ",numeros_al_final_filter([3, "a", 1, "b", 10, "j"]))
# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN

###############################################################################

def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    listint = []
    liststring = []
    if len(lista) == 0:
        return []

    if isinstance(lista[0], float) or isinstance(lista[0], int):
        listint.append(numeros_al_final_recursivo(lista[1:]))
    else:
        liststring.append(numeros_al_final_recursivo(lista[1:]))
    return (liststring + listint)
    pass # Completar


print("numeros al final by recursivo: ",numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]))
# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
