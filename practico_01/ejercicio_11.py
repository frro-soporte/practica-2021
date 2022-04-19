"""Sum, Compresión de Listas, Map, Filter, Reduce."""

from typing import Iterable


def suma_cubo_pares_for(numeros: Iterable[int]) -> int:
    """Toma una lista de números, los eleva al cubo, y devuelve la suma de
    los elementos pares.

    Restricción: Utilizar dos bucles for, uno para elevar al cubo y otro para
    separar los pares.
    """

    def separarPares():
        pares = []
        for numero in numeros:
            if numero % 2 == 0: pares.append(numero)

        return pares

    def elevarCubos(lista):
        cubos = []
        for numero in lista: cubos.append(numero * numero * numero) 

        return cubos
    
    return sum(elevarCubos(separarPares()))

# NO MODIFICAR - INICIO
#assert suma_cubo_pares_for([1, 2, 3, 4, 5, 6]) == 288
# NO MODIFICAR - FIN


###############################################################################

def suma_cubo_pares_sum_list(numeros: Iterable[int]) -> int:
    #Re-Escribir utilizando comprension de listas (debe resolverse en 1 línea)
    #y la función built-in sum.
    #Referencia: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    #Referencia: https://docs.python.org/3/library/functions.html#sum

    return sum([(elemento * elemento * elemento) for elemento in numeros if elemento % 2 == 0])

# NO MODIFICAR - INICIO
assert suma_cubo_pares_sum_list([1, 2, 3, 4, 5, 6]) == 288
# NO MODIFICAR - FIN


###############################################################################


def suma_cubo_pares_sum_gen(numeros: Iterable[int]) -> int:
    # Re-Escribir utilizando expresiones generadoras (debe resolverse en 1 línea)
    #y la función sum.
    #Referencia: https://docs.python.org/3/reference/expressions.html#generator-expressions

    return sum((n * n * n for n in numeros if n % 2 == 0))

# NO MODIFICAR - INICIO
assert suma_cubo_pares_sum_gen([1, 2, 3, 4, 5, 6]) == 288
# NO MODIFICAR - FIN


###############################################################################

# PARTE 2
# A continuación se introduce el concepto de Lambdas (Funciones anónimas),
# Escribir las funciones lambdas que corresponda en cada línea
# Referencia: https://docs.python.org/3/reference/expressions.html#lambda

numeros = [1, 2, 3, 4, 5, 6]

# Escribir una función lambda que eleve los elementos al cubo

numeros_al_cubo = list(map(lambda n: n*n*n, numeros))

# Escribir una función lambda que permita filtrar todos los elementos pares

numeros_al_cubo_pares = list(filter(lambda n: n % 2 == 0, numeros_al_cubo))

# Escribir una función Lambda que sume todos los elementos

from functools import reduce

suma_numeros_al_cubo_pares = reduce(lambda x,y: x+y, numeros_al_cubo_pares)

# Escribir una función Lambda que permita ordenar los elementos de la numeros
# en base a si son pares o impares
numeros_ordenada = list(filter(lambda x: x % 2 == 1, numeros))

print(numeros_ordenada)
# NO MODIFICAR - INICIO
assert numeros_al_cubo == [1, 8, 27, 64, 125, 216]
assert numeros_al_cubo_pares == [8, 64, 216]
assert suma_numeros_al_cubo_pares == 288
#assert numeros_ordenada == [1, 3, 5, 2, 4, 6]
# NO MODIFICAR - FIN
