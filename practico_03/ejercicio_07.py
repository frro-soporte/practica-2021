"""Deepcopy y Listas de Objetos"""

from dataclasses import dataclass
from typing import List


# NO MODIFICAR - INICIO
@dataclass
class Articulo:
    nombre: str
    precio: float

# NO MODIFICAR - FIN


from copy import deepcopy


def actualizar_precio(articulos: List[Articulo], porcentaje: float) -> List[Articulo]:
    """Toma una lista de articulos y un porcentaje, al precio de cada articulo
    le suma un porcentaje. Devuelve una lista con los precios actualizados.

    Restricción: NO se debe modificar la clase ni los tests.
    Hint: Usar deepcopy (https://docs.python.org/3/library/copy.html#copy.deepcopy)
    """
    
    # Completar
    nuevos = []
    for articulo in deepcopy(articulos):
        articulo.precio *= 1 + porcentaje / 100
        nuevos.append(articulo)
    return nuevos

# NO MODIFICAR - INICIO
nombres = ["sabana", "parlante", "computadora", "tasa", "botella", "celular"]
precios = [10.25, 5.258, 350.159, 25.99, 18.759, 215.231]

articulos = [Articulo(nombre, precio) for nombre, precio in zip(nombres, precios)]
porcentaje_aumento = 10

articulos_actualizados = actualizar_precio(articulos, porcentaje_aumento)
precios_desactualizados = [articulo.precio for articulo in articulos]
precios_actualizados = [articulo.precio for articulo in articulos_actualizados]

# Test Lista vacia
assert precios_actualizados

# Test de precios
for precio_viejo, precio_nuevo in zip(precios_desactualizados, precios_actualizados):
    assert precio_nuevo == precio_viejo * (1 + porcentaje_aumento / 100)
    
# NO MODIFICAR - FIN
