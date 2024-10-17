# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod

from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError


class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    @abstractmethod
    def es_valida(self):
        ...

    def _validar_longitud(self, clave: str) -> bool:
        longitud_clave = len(clave)
        if not longitud_clave >= self._longitud_esperada:
            raise NoCumpleLongitudMinimaError
        return True

    def _contiene_mayuscula(self, clave: str) -> bool:
        if not clave.isupper():
            raise NoTieneLetraMayusculaError
        return True

    def _contiene_minuscula(self, clave: str):
        if not clave.islower():
            raise NoTieneLetraMinusculaError
        return True
    def _contiene_numero(self, clave: str):
        if not clave.isdigit():
            raise NoTieneNumeroError
        return True

