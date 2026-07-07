from persona import Persona
from excepciones import ClienteInvalidoError
from logger import Logger


class Cliente(Persona):
    """
    Representa un cliente de Software FJ.
    Hereda de la clase abstracta Persona.
    """

    def __init__(self, nombre, documento, correo):
        super().__init__(nombre, documento)
        self.correo = correo

    # -------------------------
    # Propiedad correo
    # -------------------------
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        if not valor or "@" not in valor or "." not in valor:
            Logger.registrar_error("Correo electrónico inválido.")
            raise ClienteInvalidoError(
                "El correo electrónico ingresado no es válido."
            )

        self.__correo = valor.strip().lower()

    # -------------------------
    # Método abstracto implementado
    # -------------------------
    def mostrar_informacion(self):
        """
        Devuelve la información del cliente.
        """
        return (
            f"Nombre: {self.nombre}\n"
            f"Documento: {self.documento}\n"
            f"Correo: {self.correo}"
        )

    def __str__(self):
        """
        Representación del objeto al imprimirlo.
        """
        return f"{self.nombre} - {self.documento}"