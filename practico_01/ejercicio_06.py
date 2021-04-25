"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    count = 0
    ordered = []
    for i in lista:
        if type(i) == int:
            ordered.append(i)
        else:
            ordered.insert(count, i)
            count += 1
    return ordered


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == [
    "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""

    strings = [i for i in lista if type(i) != int]
    numbers = [i for i in lista if type(i) == int]

    return strings + numbers


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == [
    "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    return sorted(lista, key=lambda n: type(n) == int)


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == [
    "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    strings = list(filter(lambda n: type(n) != int, lista))
    numbers = list(filter(lambda n: n not in strings, lista))
    return strings + numbers


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == [
        "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################

def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""

    if all(type(i) == int for i in lista):
        return lista

    a, *b = lista
    if type(a) == int:
        b.append(a)
        return numeros_al_final_recursivo(b)
    return [a] + numeros_al_final_recursivo(b)


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == [
        "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
