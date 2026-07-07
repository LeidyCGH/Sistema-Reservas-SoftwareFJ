from logger import Logger

from excepciones import (
    ReservaInvalidaError,
    ServicioNoDisponibleError,
    DuracionInvalidaError
)


class Reserva:
    """
    Representa una reserva realizada por un cliente
    para un servicio determinado.
    """

    def __init__(self, cliente, servicio, duracion):

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo = 0

    # ---------------------------------
    # Validación inicial de la reserva
    # ---------------------------------

    def validar_reserva(self):

        if self.cliente is None:

            Logger.registrar_error(
                "Reserva sin cliente asociado."
            )

            raise ReservaInvalidaError(
                "La reserva debe tener un cliente."
            )

        if self.servicio is None:

            Logger.registrar_error(
                "Reserva sin servicio asociado."
            )

            raise ServicioNoDisponibleError(
                "La reserva debe tener un servicio."
            )

        if self.duracion <= 0:

            Logger.registrar_error(
                "Duración inválida en la reserva."
            )

            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )


    # ---------------------------------
    # Procesamiento de reserva
    # ---------------------------------

    def procesar(self):

        try:

            self.validar_reserva()

            self.costo = self.servicio.calcular_costo(
                self.duracion
            )


        except (
            ServicioNoDisponibleError,
            DuracionInvalidaError,
            ReservaInvalidaError
        ) as error:

            Logger.registrar_error(
                f"Error procesando reserva: {error}"
            )

            raise ReservaInvalidaError(
                "La reserva no pudo ser procesada."
            ) from error


        except Exception as error:

            Logger.registrar_error(
                f"Error inesperado: {error}"
            )

            raise ReservaInvalidaError(
                "Ocurrió un error inesperado."
            ) from error


        else:

            self.confirmar()

            Logger.registrar_evento(
                "Reserva procesada correctamente."
            )

            return self.costo


        finally:

            Logger.registrar_evento(
                "Finalizó el intento de procesamiento de reserva."
            )


    # ---------------------------------
    # Confirmar reserva
    # ---------------------------------

    def confirmar(self):

        self.estado = "Confirmada"

        Logger.registrar_evento(
            f"Reserva confirmada para {self.cliente.nombre}"
        )


    # ---------------------------------
    # Cancelar reserva
    # ---------------------------------

    def cancelar(self):

        self.estado = "Cancelada"

        Logger.registrar_evento(
            f"Reserva cancelada para {self.cliente.nombre}"
        )


    # ---------------------------------
    # Mostrar información
    # ---------------------------------

    def mostrar_reserva(self):

        return (
            "\n===== INFORMACIÓN DE RESERVA ====="
            f"\nCliente: {self.cliente.nombre}"
            f"\nServicio: {self.servicio.nombre}"
            f"\nDescripción: {self.servicio.descripcion()}"
            f"\nDuración: {self.duracion}"
            f"\nCosto: ${self.costo}"
            f"\nEstado: {self.estado}"
        )