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
    todos.extend(strings)
    todos.extend(numeros)
    return todos

# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""
    numeros=[num for num in lista if type(num)!=str]
    strings=[cad for cad in lista if type(cad)==str]
    strings.extend(numeros)
    return strings

# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    return sorted(lista, key=lambda x:  type(x)!=str)

# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    todos=list(filter(lambda a: type(a)==str, lista))
    todos.extend(list(filter(lambda a: a not in todos, lista)))
    return todos

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN

"""Solución alternativa, donde se utiliza la misma nomenclatura del ejercicio anterior
def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    todos=list(filter(lambda a: type(a)==str, lista))
    todos.extend(list(filter(lambda x:  type(x)!=str, lista)))
    return todos"""


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    if all(type(i) == int for i in lista):
        return lista
    
    a,*b=lista
    if type(a) == int:
        b.append(a)
        return numeros_al_final_recursivo(b)
    return [a] + numeros_al_final_recursivo(b)

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
