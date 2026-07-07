from abc import ABC, abstractmethod
from excepciones import ClienteInvalidoError
from logger import Logger


class Persona(ABC):
    """
    Clase abstracta que representa una persona del sistema.
    """

    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    # -------------------------
    # Propiedad nombre
    # -------------------------
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor or not valor.strip():
            Logger.registrar_error("El nombre está vacío.")
            raise ClienteInvalidoError(
                "El nombre no puede estar vacío."
            )

        self.__nombre = valor.strip().title()

    # -------------------------
    # Propiedad documento
    # -------------------------
    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):

        valor = str(valor).strip()

        if not valor.isdigit():
            Logger.registrar_error(
                "Documento con caracteres no válidos."
            )
            raise ClienteInvalidoError(
                "El documento solo debe contener números."
            )

        self.__documento = valor

    # -------------------------
    # Método abstracto
    # -------------------------
    @abstractmethod
    def mostrar_informacion(self):
        """
        Cada clase hija deberá implementar este método.
        """
        pass