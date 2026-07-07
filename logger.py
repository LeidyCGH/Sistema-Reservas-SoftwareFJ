from datetime import datetime


class Logger:
    """
    Clase encargada de registrar eventos y errores del sistema
    en el archivo logs.txt.
    """

    ARCHIVO_LOG = "logs.txt"

    @staticmethod
    def registrar_evento(mensaje):
        """Registra un evento normal."""
        with open(Logger.ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            archivo.write(f"[{fecha}] EVENTO: {mensaje}\n")

    @staticmethod
    def registrar_error(mensaje):
        """Registra un error."""
        with open(Logger.ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            archivo.write(f"[{fecha}] ERROR: {mensaje}\n")
            