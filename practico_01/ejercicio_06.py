"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(
        lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    lista2: List[Union[float, str]] = []
    j = 0
    for i in range(0, len(lista)):
        if isinstance(lista[i], str):
            lista2.insert(j, lista[i])
            j += 1
        elif isinstance(lista[i], int):
            lista2.append(lista[i])
    return lista2


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == [
    "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(
        lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""

    lista2 = [n for n in lista if isinstance(n, str)]
    lista3 = [n for n in lista if isinstance(n, int)]
    return lista2 + lista3


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == [
    "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(
        lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    return sorted(lista, key=lambda x: not isinstance(x, str))


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == [
    "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(
        lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    lista1 = list(filter(lambda x: isinstance(x, str), lista))
    lista2 = list(filter(lambda x: isinstance(x, int), lista))
    return lista1 + lista2


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == [
        "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(
        lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    if all(isinstance(i, int) for i in lista):
        return lista
    a, *b = lista
    if isinstance(a, int):
        b.append(a)
        return numeros_al_final_recursivo(b)
    return [a] + numeros_al_final_recursivo(b)


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == [
        "a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
