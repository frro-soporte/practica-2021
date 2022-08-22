# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):
    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        socio = DatosSocio.buscar(self, id_socio)
        return socio

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        socio_dni = DatosSocio.buscar_dni(dni_socio)
        return socio_dni

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return DatosSocio.todos(self)

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        if self.regla_1(socio) and self.regla_2(socio) and self.regla_3():
            DatosSocio.alta(self, socio)
            return True
        return False

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        if DatosSocio.baja(self, id_socio):
            return True
        return False

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        if self.regla_2(socio):
            DatosSocio.modificacion(self, socio)
            return True
        return False

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        socio_existente = DatosSocio.buscar_dni(self, socio.dni)

        if socio_existente is None:
            return True
        else:
            raise DniRepetido()
            return False

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if self.MIN_CARACTERES < len(socio.nombre) < self.MAX_CARACTERES \
                and self.MIN_CARACTERES < len(socio.apellido) < self.MAX_CARACTERES:
            return True
        else:
            raise LongitudInvalida()
            return False

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if DatosSocio.contarSocios(self) < self.MAX_SOCIOS:
            return True
        else:
            raise MaximoAlcanzado()
            return False
