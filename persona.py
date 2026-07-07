from abc import ABC
from excepciones import ClienteInvalidoError
from logger import Logger


class Persona(ABC):
    """
    Clase abstracta que representa una persona del sistema.
    """

    def __init__(self, nombre, documento):

        self.nombre = nombre
        self.documento = documento

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor.strip():
            Logger.registrar_error("Nombre vacío.")

            raise ClienteInvalidoError(
                "El nombre no puede estar vacío."
            )

        self.__nombre = valor.title()

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):

        if not valor.isdigit():

            Logger.registrar_error(
                "Documento inválido."
            )

            raise ClienteInvalidoError(
                "El documento solo debe contener números."
            )

        self.__documento = valor