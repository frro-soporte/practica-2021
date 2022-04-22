"""Comparaciones Encadenadas, Cantidad Arbitraria de Parámetros, Recursividad."""


def maximo_encadenado(a: float, b: float, c: float) -> float:
    """Toma 3 números y devuelve el máximo.
    Restricción: Utilizar UNICAMENTE tres IFs y comparaciones encadenadas.
    Referencia: https://docs.python.org/3/reference/expressions.html#comparisons
    """

    if b < a > c:
        return a
    elif a < b > c:
        return b  
    return c


# NO MODIFICAR - INICIO
assert maximo_encadenado(1, 10, 5) == 10
assert maximo_encadenado(4, 9, 18) == 18
assert maximo_encadenado(24, 9, 18) == 24
# NO MODIFICAR - FIN


###############################################################################


def maximo_cuadruple(a: float, b: float, c: float, d: float) -> float:
    """Re-escribir para que tome 4 parámetros, utilizar la función max.
    Referencia: https://docs.python.org/3/library/functions.html#max"""

    return max(a, b, c, d)


# NO MODIFICAR - INICIO
assert maximo_cuadruple(1, 10, 5, -5) == 10
assert maximo_cuadruple(4, 9, 18, 6) == 18
assert maximo_cuadruple(24, 9, 18, 20) == 24
assert maximo_cuadruple(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################


def maximo_arbitrario(*args) -> float:
    """Re-escribir para que tome una cantidad arbitraria de parámetros.
    Referencia: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
    """
    return max(*args)



# NO MODIFICAR - INICIO
assert maximo_arbitrario(1, 10, 5, -5) == 10
assert maximo_arbitrario(4, 9, 18, 6) == 18
assert maximo_arbitrario(24, 9, 18, 20) == 24
assert maximo_arbitrario(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################


def maximo_recursivo(*args) -> float:
    """Re-Escribir de forma recursiva."""

    if len(args) <= 1:
      return args[0]
    else: 
      m = maximo_recursivo(args[1:])
      print(m)
      return m if 1>args[0] else args[0]


# NO MODIFICAR - INICIO
#assert maximo_recursivo(1, 10, 5, -5) == 10
#assert maximo_recursivo(4, 9, 18, 6) == 18
#assert maximo_recursivo(24, 9, 18, 20) == 24
#assert maximo_recursivo(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN
