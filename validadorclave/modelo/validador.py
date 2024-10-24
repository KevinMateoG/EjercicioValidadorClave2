# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod
from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        for letra in clave:
            if letra.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave: str) -> bool:
        for letra in clave:
            if letra.islower():
                return True
        return False

    def _contiene_numero(self, clave: str) -> bool:
        for letra in clave:
            if letra.isdigit():
                return True
        return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        ...


class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str):
        for letra in clave:
            if letra in "@_#$%":
                return True
        return False

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La longitud minima es de 8 caracteres")
        elif not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("debe tener una mayuscula")
        elif not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("debe teenr una minuscula")
        elif not self._contiene_numero(clave):
            raise NoTieneNumeroError("debe tener un nuemro")
        elif not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("Debe tener caracter especial")
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:
        copia: str = clave.lower()
        palabra: str = "calisto"
        index_calisto = 0
        while index_calisto + len(palabra) <= len(clave):
            index_calisto = copia.find(palabra, index_calisto)
            if index_calisto >= 0:
                pi = index_calisto
                pf = index_calisto + len(palabra)
                palabra_original = clave[pi:pf]

                cont_mayusculas = 0
                for letra in palabra_original:
                    if letra.isupper():
                        cont_mayusculas += 1

                if 2 <= cont_mayusculas < len(palabra):
                    return True
                else:
                    index_calisto += len(palabra)
            else:
                return False
        return False

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La longitud minima es de 6 caracteres")
        elif not self._contiene_mayuscula(clave):
            raise NoTieneNumeroError("debe tener un numero")
        elif not self.contiene_calisto(clave):
            raise NoTieneCaracterEspecialError("Debe tener la palabra calisto con lo menos 2 mayusculas")
        return True
class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave) -> bool:
        return self.regla.es_valida(clave)