def maximo_basico(a: float, b: float):
    if a > b: return a
    return b

# NO MODIFICAR - INICIO
assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18
# NO MODIFICAR - FIN

###############################################################################

def maximo_libreria(a: float, b: float) -> float:
    return max([a, b])

# NO MODIFICAR - INICIO
assert maximo_libreria(10, 5) == 10
assert maximo_libreria(9, 18) == 18
# NO MODIFICAR - FIN

###############################################################################

def maximo_ternario(a: float, b: float) -> float:
    return a if a > b else b

# NO MODIFICAR - INICIO
assert maximo_ternario(10, 5) == 10
assert maximo_ternario(9, 18) == 18
# NO MODIFICAR - FIN
