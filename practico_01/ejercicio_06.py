"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union

from numpy.core.defchararray import isnumeric


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    pass # Completar
    numberList =[]
    charList = []

    for i in range(len(lista)):
        if str(lista[i]).isdigit():
            numberList.append(lista[i])
        else:
            charList.append(lista[i])

    return charList+numberList



# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""
    pass # Completar

    numberList = [element for element in lista if str(element).isdigit()]
    charList = [element for element in lista if not(str(element).isdigit())]

    return charList + numberList




# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    pass # Completar

    return sorted(lista, key=lambda element: str(element).isdigit())

# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    pass # Completar

    numberList = list(filter(lambda element: str(element).isdigit(), lista))
    charList = list(filter(lambda element: not(str(element).isdigit()), lista))

    return charList + numberList

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    pass # Completar

    if all(type(item) == int for item in lista):  # Verificar que la lista tenga solo int
        return lista

    a, *b = lista  # guarda el primer elemento en a
    if type(a) == int:
        b.append(a)
        return numeros_al_final_recursivo(b)
    return [a] + numeros_al_final_recursivo(b)

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
