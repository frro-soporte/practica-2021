"""Slicing."""


def es_palindromo(palabra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si se lee igual al
    derecho y al revés.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    if len(palabra) == 0:
        return  False
    if palabra[0] == palabra[len(palabra)- 1]:
        return True
    else:
        return False
    pass # Completar


print("Es un palíndromo : ",es_palindromo("radar"))
# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
#assert es_palindromo("")
# NO MODIFICAR - FIN

###############################################################################

def mitad(palabra: str) -> str:
    """Toma un string y devuelve la mitad. Si la longitud es impar, redondear
    hacia arriba.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    pal = palabra
    if len(palabra) == 0:
        return False
    lon = len(palabra)
    if lon % 2 != 0:
        return palabra[:int(lon/2) + 1]
    else:
        return palabra[:int(lon/2)]
    pass # Completar

print("Cortar por la mitad : ",mitad("hel"))
# NO MODIFICAR - INICIO
assert mitad == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
