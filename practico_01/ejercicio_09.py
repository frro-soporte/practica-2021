"""FOR, Sum, Reduce."""

def sumatoria_basico(n: int) -> int:
    #Devuelve la suma de los números de 1 a N.
    #Restricción: Utilizar un bucle for.
    total = 0
    for x in range(n + 1):
        total = total + x

    return total
# NO MODIFICAR - INICIO
assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050
# NO MODIFICAR - FIN

###############################################################################


def sumatoria_sum(n: int) -> int:
    #Re-Escribir utilizando la función sum y sin usar bucles.
    #Referencia: https://docs.python.org/3/library/functions.html#sum
    """
    Alternativa 1:

    def acumular(iteracion, acumulado):
        return acumulado if iteracion == 0 else acumular(iteracion - 1, (acumulado + iteracion - 1))

    return n if n in [1, 0] else acumular(n, n)
    
    Alternativa 2:

    lista = []
    def generarLista(it):
        if it == 0: return lista
        else:
            lista.append(it)
            generarLista(it - 1)

    generarLista(n)
    return sum(lista)

    Alternativa 3:
    return sum(range(n+1))
    """

    return sum(range(n))+n

# NO MODIFICAR - INICIO
assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050
# NO MODIFICAR - FIN


###############################################################################

from functools import reduce

def sumatoria_reduce(n: int) -> int:
    #CHALLENGE OPCIONAL: Re-escribir utilizando reduce.
    #Referencia: https://docs.python.org/3/library/functools.html#functools.reduce
    if n == 1 or n == 0: return n
    else: return reduce(lambda x, y: x + y, range(n+1))

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert sumatoria_reduce(1) == 1
    assert sumatoria_reduce(100) == 5050
# NO MODIFICAR - FIN


###############################################################################

def sumatoria_gauss(n: int) -> int:
    #CHALLENGE OPCIONAL: Re-Escribir utilizando suma de Gauss.
    #Referencia: https://es.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
    return (n*(n+1))//2

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert sumatoria_gauss(1) == 1
    assert sumatoria_gauss(100) == 5050
# NO MODIFICAR - FIN
