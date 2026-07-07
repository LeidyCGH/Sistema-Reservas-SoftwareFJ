from abc import ABC, abstractmethod
from logger import Logger
from excepciones import (
    ServicioNoDisponibleError,
    DuracionInvalidaError
)


class Servicio(ABC):
    """
    Clase abstracta para representar un servicio de Software FJ.
    """

    def __init__(self, nombre, tarifa):

        self.nombre = nombre
        self.tarifa = tarifa

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor.strip():

            Logger.registrar_error("Nombre del servicio vacío.")

            raise ServicioNoDisponibleError(
                "El servicio debe tener un nombre."
            )

        self.__nombre = valor

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, valor):

        if valor <= 0:

            Logger.registrar_error("Tarifa inválida.")

            raise ServicioNoDisponibleError(
                "La tarifa debe ser mayor que cero."
            )

        self.__tarifa = valor

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def validar(self, duracion):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar(duracion)

        subtotal = self.tarifa * duracion
        total = subtotal + impuesto - descuento

        return total

    def descripcion(self):

        return f"Reserva de sala - ${self.tarifa} por hora"

    def validar(self, duracion):

        if duracion <= 0:

            Logger.registrar_error(
                "Duración inválida para reserva de sala."
            )

            raise DuracionInvalidaError(
                "Las horas deben ser mayores que cero."
            )


class AlquilerEquipo(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar(duracion)

        subtotal = self.tarifa * duracion
        total = subtotal + impuesto - descuento

        return total

    def descripcion(self):

        return f"Alquiler de equipos - ${self.tarifa} por día"

    def validar(self, duracion):

        if duracion <= 0:

            Logger.registrar_error(
                "Duración inválida para alquiler."
            )

            raise DuracionInvalidaError(
                "Los días deben ser mayores que cero."
            )


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar(duracion)

        subtotal = self.tarifa * duracion
        total = subtotal + impuesto - descuento

        return total

    def descripcion(self):

        return f"Asesoría especializada - ${self.tarifa} por hora"

    def validar(self, duracion):

        if duracion <= 0:

            Logger.registrar_error(
                "Duración inválida para asesoría."
            )

            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )