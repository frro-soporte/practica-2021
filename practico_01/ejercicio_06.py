"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    numeros=[]
    strings=[]
    todos=[]
    for valor in lista:
        if type(valor)==int:
            numeros.append(valor)
        else:
            strings.append(valor)
    for string in strings:
        todos.append(string)
    for num in numeros:
        todos.append(num)
    return todos

# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""
    numeros=[]
    for valor in lista:
        if type(valor)==int:
            lista.remove(valor)
            numeros.append(valor)
    for num in numeros:
        lista.append(num)
    return lista


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    listaOrdenada=sorted(lista, key=str, reverse=True)
    print(listaOrdenada)
    return listaOrdenada
    #no funciona

# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    def getStrings(valor):
        if type(valor)==str:
            return True
    def getNumeros(valor):
        if type(valor)==int:
            return True

    strings=list(filter(getStrings, lista))
    numeros=list(filter(getNumeros, lista))
    for num in numeros:
        strings.append(num)
    return strings

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    def cargarLista(tipo: object, listaTotal: List[Union[float, str]]) -> List[Union[float, str]]:
        for valor in lista:
                if type(valor)==tipo:
                    listaTotal.append(valor)
        if tipo!=int:
            cargarLista(int, listaTotal)
        return listaTotal

    listaTotal=[]
    return cargarLista(str, listaTotal)

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
