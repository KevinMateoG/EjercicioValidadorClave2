# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod

from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError


class ReglaValidacion(ABC):
    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    @abstractmethod
    def es_valida(self, clave: str):
        ...

    def _validar_longitud(self, clave: str) -> bool:
        longitud_clave = len(clave)
        if not longitud_clave >= self._longitud_esperada:
            raise NoCumpleLongitudMinimaError()
        return True

    def _contiene_mayuscula(self, clave: str) -> bool:
        if not clave.isupper():
            raise NoTieneLetraMayusculaError()
        return True

    def _contiene_minuscula(self, clave: str) -> bool:
        if not clave.islower():
            raise NoTieneLetraMinusculaError()
        return True

    def _contiene_numero(self, clave: str) -> bool:
        if not clave.isdigit():
            raise NoTieneNumeroError()
        return True




class ReglaValidacionGanimedes(ReglaValidacion):
    def contiene_caracter_especial(self, clave: str):
        if not "@" or "_" or "#" or "$" or "%" in clave:
            raise NoTieneCaracterEspecialError()
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave: str):
        calisto = {"C": "a",
                 "A": "b",
                 "l": "c",
                "I":"i",
                   "S": "s",
                   "T": "t",
                   "O": "o"}
        pass

class Validador(ReglaValidacion):
    def __init__(self, regla: ReglaValidacion, _longitud_esperada: int):
        super().__init__(_longitud_esperada)
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        pass