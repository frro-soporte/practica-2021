"""Expresiones Booleanas."""


from re import A


def es_vocal_if(letra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si letra es una vocal o
    no.

    Restricción: Utilizar un if para cada posibilidad con la función lower().
    Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods
    """
    if letra == 'A' or letra.lower() =="a":
        boleanRta = True
        if  letra == 'E' or letra.lower() =='e':
            boleanRta = True
            if  letra == 'I' or letra.lower() =='i':
                boleanRta = True
                if  letra == 'O' or letra.lower() =='o':
                    boleanRta = True
                    if  letra == 'U' or letra.lower() =='u':
                        boleanRta = True
    else:
        boleanRta = False
    return boleanRta
# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    """Re-escribir utilizando un sólo IF y el operador IN.
    Referencia: https://docs.python.org/3/reference/expressions.html#membership-test-operations
    """
    if (letra in ('A','a','E','e','I','i','O','o','U','u')):
        rtaBool= True
    else: 
        rtaBool = False
    return rtaBool



# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    """Re-escribir utilizando el operador IN pero sin utilizar IF."""
    return letra in ('A','a','E','e','I','i','O','o','U','u')
    pass # Completar


# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
