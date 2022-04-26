"""Tuple, Enumerate, Zip, Args.


Contexto: Se tiene un programa que lee diferentes listas de una tabla en una
base de datos y se quieren combinar estas listas para que luego puedan crearse
los objetos de la capa de negocio.
"""


from re import L
from typing import Any, List, Tuple

nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]


def combinar_basico(nombres: List[str], precios: List[float]) -> Tuple[Any]:
    #Toma dos listas y devuelve una tupla de duplas con los componentes de
    #las listas. Restricción: Resolver utilizando un bucle for.
    res = []
    for idx in range(len(nombres)):
        res.append((nombres[idx], precios[idx]))
        
    return tuple(res)

# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48),
    ("lámpara", 16.42),
    ("shampoo", 5.20),
)

assert combinar_basico(nombre_articulos, precio_articulos) == respuesta
# NO MODIFICAR - FIN

###############################################################################


id_articulos = [6852, 1459, 3578]


def combinar_enumerate(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:
    #Re-Escribir utilizando enumerate y agregando un nuevo componente.
    #Referencia: https://docs.python.org/3/library/functions.html#enumerate
    # Alternativa: return tuple((p1, p2, p3) for idx1, p1 in enumerate(nombres) for idx2, p2 in enumerate(precios)for idx3, p3 in enumerate(ids) if idx1 == idx2 == idx3)

    lista = []
    for idx, id in enumerate(ids):
        lista.append((nombres[idx], precios[idx], id))

    return(tuple(lista))

# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar_enumerate(nombre_articulos, precio_articulos, id_articulos) == respuesta
# NO MODIFICAR - FIN


###############################################################################

id_articulos = [6852, 1459, 3578]


def combinar_zip(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:
    #Re-Escribir utilizando zip.
    #Referencia: https://docs.python.org/3/library/functions.html#zip
    return tuple(list(zip(nombres, precios, ids)))

# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar_zip(nombre_articulos, precio_articulos, id_articulos) == respuesta
# NO MODIFICAR - FIN


###############################################################################

#nombre_articulos = ["ventana", "lámpara", "shampoo"]
#precio_articulos = [100.48, 16.42, 5.20]
id_articulos = [6852, 1459, 3578]
categoria_articulos = ["hogar", "libreria", "perfumeria"]
importado_articulos = [True, False, True]


def combinar_zip_args(*args) -> Tuple[Any]:
    #Re-Escribir utilizando zip y una cantidad arbitraria de componentes.
    #Referencia: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
    return tuple(zip(*args))

# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852, "hogar", True),
    ("lámpara", 16.42, 1459, "libreria", False),
    ("shampoo", 5.2, 3578, "perfumeria", True),
)

componentes = [
    nombre_articulos,
    precio_articulos,
    id_articulos,
    categoria_articulos,
    importado_articulos,
]

assert combinar_zip_args(*componentes) == respuesta
# NO MODIFICAR - FIN
