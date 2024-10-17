# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod

from validadorclave.modelo.errores import NoCumpleLongitudMinimaError


class ReglaValidacion(ABC):
    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    @abstractmethod
    def es_valida(self):
        ...

    def _validar_longitud(self):
        if not self._longitud_esperada >= 8:
            raise NoCumpleLongitudMinimaError("No cumples con la longitud")
