"""Único return vs múltiples return."""

from typing import Union


def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    """Toma dos números (a, b) y un booleano (multiplicar):
        - Si multiplicar es True: devuelve la multiplicación entre a y b.
        - Si multiplicar es False: devuelve la division entre a y b.
        - Si multiplicar es False y b es cero: devuelve "Operación no válida".

    Restricciones:
        - Utilizar un único return.
        - No utilizar AND ni OR.
    """
    valreturn = "";
    if multiplicar:
        valreturn = (a * b)
    elif multiplicar == False:
        if b > 0:
            valreturn = (a / b)
        else:
            valreturn = "Operación no válida"

    return valreturn
   


print("Operacion basico sin usar ni And, ni OR con un solo return: ", operacion_basica(25, 0, False))
# NO MODIFICAR - INICIO
assert operacion_basica(1, 1, True) == 1
assert operacion_basica(1, 1, False) == 1
assert operacion_basica(25, 5, True) == 125
assert operacion_basica(25, 5, False) == 5
assert operacion_basica(0, 5, True) == 0
assert operacion_basica(0, 5, False) == 0
assert operacion_basica(1, 0, True) == 0
assert operacion_basica(1, 0, False) == "Operación no válida"


# NO MODIFICAR - FIN
###############################################################################


def operacion_multiple(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    """Re-Escribir utilizando tres returns."""
    if multiplicar:
        return a * b
    elif multiplicar == False and b > 0:
        return a / b
    else:
        return "Operación no válida"
  
print("Operacion multiple con varios return: ", operacion_multiple(25, 0, False))
# NO MODIFICAR - INICIO
assert operacion_multiple(1, 1, True) == 1
assert operacion_multiple(1, 1, False) == 1
assert operacion_multiple(25, 5, True) == 125
assert operacion_multiple(25, 5, False) == 5
assert operacion_multiple(0, 5, True) == 0
assert operacion_multiple(0, 5, False) == 0
assert operacion_multiple(1, 0, True) == 0
assert operacion_multiple(1, 0, False) == "Operación no válida"
# NO MODIFICAR - FIN