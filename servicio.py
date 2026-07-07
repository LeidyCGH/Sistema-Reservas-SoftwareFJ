from abc import ABC, abstractmethod

from excepciones import (
    ServicioNoDisponibleError,
    DuracionInvalidaError
)

from logger import Logger


class Servicio(ABC):
    """
    Clase abstracta que representa un servicio
    ofrecido por Software FJ.
    """

    def __init__(self, nombre, tarifa):

        self.nombre = nombre
        self.tarifa = tarifa

    # -------------------------
    # Propiedad nombre
    # -------------------------

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor or not valor.strip():

            Logger.registrar_error(
                "El nombre del servicio está vacío."
            )

            raise ServicioNoDisponibleError(
                "Debe ingresar un nombre para el servicio."
            )

        self.__nombre = valor.strip().title()

    # -------------------------
    # Propiedad tarifa
    # -------------------------

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, valor):

        if valor <= 0:

            Logger.registrar_error(
                "Tarifa inválida."
            )

            raise ServicioNoDisponibleError(
                "La tarifa debe ser mayor que cero."
            )

        self.__tarifa = valor

    # -------------------------
    # Métodos abstractos
    # -------------------------

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """
        Calcula el costo total del servicio.
        """
        pass

    @abstractmethod
    def descripcion(self):
        """
        Devuelve la descripción del servicio.
        """
        pass

    @abstractmethod
    def validar_duracion(self, duracion):
        """
        Valida la duración del servicio.
        """
        pass


# ===========================================================
# Reserva de Sala
# ===========================================================

class ReservaSala(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_duracion(duracion)

        subtotal = self.tarifa * duracion
        return subtotal + impuesto - descuento

    def descripcion(self):

        return (
            f"Reserva de sala por horas "
            f"(${self.tarifa}/hora)"
        )

    def validar_duracion(self, duracion):

        if duracion <= 0:

            Logger.registrar_error(
                "Horas inválidas para reserva."
            )

            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )


# ===========================================================
# Alquiler de Equipos
# ===========================================================

class AlquilerEquipo(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_duracion(duracion)

        subtotal = self.tarifa * duracion

        if duracion >= 5:
            subtotal *= 0.90

        return subtotal + impuesto - descuento

    def descripcion(self):

        return (
            f"Alquiler de equipos "
            f"(${self.tarifa}/día)"
        )

    def validar_duracion(self, duracion):

        if duracion <= 0:

            Logger.registrar_error(
                "Días inválidos para alquiler."
            )

            raise DuracionInvalidaError(
                "Los días deben ser mayores que cero."
            )


# ===========================================================
# Asesoría Especializada
# ===========================================================

class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        self.validar_duracion(duracion)

        subtotal = self.tarifa * duracion

        if duracion >= 8:
            subtotal *= 0.85

        return subtotal + impuesto - descuento

    def descripcion(self):

        return (
            f"Asesoría especializada "
            f"(${self.tarifa}/hora)"
        )

    def validar_duracion(self, duracion):

        if duracion <= 0:

            Logger.registrar_error(
                "Duración inválida para asesoría."
            )

            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )