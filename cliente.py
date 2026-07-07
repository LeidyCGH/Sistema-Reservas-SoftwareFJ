from persona import Persona
from excepciones import ClienteInvalidoError
from logger import Logger


class Cliente(Persona):

    def __init__(self, nombre, documento, correo):

        super().__init__(nombre, documento)

        self.correo = correo

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        if "@" not in valor or "." not in valor:

            Logger.registrar_error(
                "Correo electrónico inválido."
            )

            raise ClienteInvalidoError(
                "El correo electrónico no es válido."
            )

        self.__correo = valor.lower()

    def mostrar_datos(self):

        return (
            f"Cliente: {self.nombre}\n"
            f"Documento: {self.documento}\n"
            f"Correo: {self.correo}"
        )