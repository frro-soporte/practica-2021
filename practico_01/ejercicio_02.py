"""Comparaciones Encadenadas, Cantidad Arbitraria de Parámetros, Recursividad."""


def maximo_encadenado(a: float, b: float, c: float) -> float:
    """Toma 3 números y devuelve el máximo.

    Args:
        a (float): Primer nro a comparar
        b(float): Segundo nro a comparar
        c(float): Tercer nro a comparar
    
    Returns:
        float: mayor de los tres numeros
    """
    if a > b or a == b:
        if a > c or a == c:
            return a
        else:
            return c
    else:
        if b > c or b == c:
            return b
        else:
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

    return (max(a,b,c,d))

    pass # Completar


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
    return(max(args))
    
    pass # Completar


# NO MODIFICAR - INICIO
assert maximo_arbitrario(1, 10, 5, -5) == 10
assert maximo_arbitrario(4, 9, 18, 6) == 18
assert maximo_arbitrario(24, 9, 18, 20) == 24
assert maximo_arbitrario(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################


def maximo_recursivo(*args) -> float:
    """Re-Escribir de forma recursiva."""
    
    
    if len(args)!=1:
        a,b, *c = args 
            
        if a>b: 
               
            c.insert(0,a)
            maximo_recursivo(c)
        else:
            c.insert(0,b)
            maximo_recursivo(c)
    else:
        x=args[0]
        
        if len(x)!=1:
            a,b, *c = x 
            
            if a>b: 
               
                c.insert(0,a)
                maximo_recursivo(c)
            else:
                c.insert(0,b)
                maximo_recursivo(c)
        elif len(x)==1:
            print(x[0])
    
        

maximo_recursivo(1, 10, 5, -5)
maximo_recursivo(4, 9, 18, 6) 
maximo_recursivo(24, 9, 18, 20)
maximo_recursivo(24, 9, 18, 30)
# NO MODIFICAR - INICIO
assert maximo_recursivo(1, 10, 5, -5) == 10
assert maximo_recursivo(4, 9, 18, 6) == 18
assert maximo_recursivo(24, 9, 18, 20) == 24
assert maximo_recursivo(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN
