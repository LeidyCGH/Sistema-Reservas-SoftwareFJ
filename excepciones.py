class ErrorSistema(Exception):
    """
    Excepción base del sistema.
    Todas las demás excepciones heredarán de esta.
    """
    pass


class ClienteInvalidoError(ErrorSistema):
    """Se genera cuando los datos del cliente son inválidos."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no puede utilizarse."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se genera cuando una reserva presenta errores."""
    pass


class DuracionInvalidaError(ErrorSistema):
    """Se genera cuando la duración ingresada es incorrecta."""
    pass
