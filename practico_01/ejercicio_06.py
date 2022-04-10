"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union

def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    letras = []
    numeros = []
    ordenados = []
    for elemento in lista:
        tipo = type(elemento)
        if tipo == str: letras.append(elemento)
        elif tipo == int or tipo == float: numeros.append(elemento)
    
    for letra in letras: ordenados.append(letra)
    for numero in numeros: ordenados.append(numero)
    return ordenados

# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN

###############################################################################

def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    #Re-escribir utilizando comprensión de listas.
    letras = [elemento for elemento in lista if type(elemento) == str]
    numeros = [elemento for elemento in lista if type(elemento) == int or type(elemento) == float]
    return [elemento for elemento in letras + numeros]

# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN

###############################################################################

def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    #Re-escribir utilizando la función sorted con una custom key.
    #Referencia: https://docs.python.org/3/library/functions.html#sorted
    def convertirLetra(el):
        #if type(el) == int: return str(el)
        #else: return el
        return str(el)
    
    lista.sort(key=convertirLetra)
    print('Log', lista)

numeros_al_final_sorted([3, "a", 1, "b", 10, "j"])
"""
# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    #CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    #Referencia: https://docs.python.org/3/library/functions.html#filter

    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    #CHALLENGE OPCIONAL - Re-escribir de forma recursiva.
    #pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
"""