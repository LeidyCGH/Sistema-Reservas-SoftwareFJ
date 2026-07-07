from cliente import Cliente

from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from reserva import Reserva

from logger import Logger


def ejecutar_operaciones():
    """
    Ejecuta las pruebas generales del sistema.
    """

    clientes = []
    servicios = []
    reservas = []

    print("\n===================================")
    print(" SISTEMA INTEGRAL SOFTWARE FJ ")
    print("===================================\n")


    # ==================================================
    # OPERACIÓN 1 - Crear cliente válido
    # ==================================================

    try:

        cliente1 = Cliente(
            "Leidy Gonzalez",
            "123456789",
            "lgherna1@gmail.com"
        )

        clientes.append(cliente1)

        print("✓ Cliente creado correctamente")


    except Exception as error:

        Logger.registrar_error(str(error))
        print(error)



    # ==================================================
    # OPERACIÓN 2 - Crear cliente con correo inválido
    # ==================================================

    try:

        cliente_error = Cliente(
            "Carlos Perez",
            "987654321",
            "correoincorrecto"
        )

        clientes.append(cliente_error)


    except Exception as error:

        Logger.registrar_error(str(error))
        print("\nError cliente:",
              error)



    # ==================================================
    # OPERACIÓN 3 - Crear servicio sala
    # ==================================================

    try:

        sala = ReservaSala(
            "Sala de juntas",
            50000
        )

        servicios.append(sala)

        print("✓ Servicio sala creado")


    except Exception as error:

        Logger.registrar_error(str(error))



    # ==================================================
    # OPERACIÓN 4 - Crear servicio equipo
    # ==================================================

    try:

        equipo = AlquilerEquipo(
            "Video Beam",
            70000
        )

        servicios.append(equipo)

        print("✓ Servicio equipo creado")


    except Exception as error:

        Logger.registrar_error(str(error))



    # ==================================================
    # OPERACIÓN 5 - Crear asesoría
    # ==================================================

    try:

        asesoria = AsesoriaEspecializada(
            "Asesoría Python",
            120000
        )

        servicios.append(asesoria)

        print("✓ Servicio asesoría creado")


    except Exception as error:

        Logger.registrar_error(str(error))



    # ==================================================
    # OPERACIÓN 6 - Reserva exitosa
    # ==================================================

    try:

        reserva1 = Reserva(
            cliente1,
            sala,
            3
        )

        reserva1.procesar()

        reservas.append(reserva1)

        print(reserva1.mostrar_reserva())


    except Exception as error:

        Logger.registrar_error(str(error))



    # ==================================================
    # OPERACIÓN 7 - Reserva con duración inválida
    # ==================================================

    try:

        reserva_error = Reserva(
            cliente1,
            equipo,
            -2
        )

        reserva_error.procesar()


    except Exception as error:

        Logger.registrar_error(str(error))

        print(
            "\nError reserva:",
            error
        )



    # ==================================================
    # OPERACIÓN 8 - Reserva sin servicio
    # ==================================================

    try:

        reserva_error2 = Reserva(
            cliente1,
            None,
            2
        )

        reserva_error2.procesar()


    except Exception as error:

        Logger.registrar_error(str(error))

        print(
            "\nError servicio:",
            error
        )



    # ==================================================
    # OPERACIÓN 9 - Aplicación de descuento
    # ==================================================

    try:

        costo = asesoria.calcular_costo(
            8,
            impuesto=10000,
            descuento=20000
        )

        print(
            "\nCosto asesoría con descuento:",
            costo
        )


    except Exception as error:

        Logger.registrar_error(str(error))



    # ==================================================
    # OPERACIÓN 10 - Cancelar reserva
    # ==================================================

    try:

        reserva1.cancelar()

        print(
            "\nReserva cancelada correctamente"
        )


    except Exception as error:

        Logger.registrar_error(str(error))



    # ==================================================
    # Resumen final
    # ==================================================

    print("\n========== RESUMEN ==========")

    print(
        f"Clientes registrados: {len(clientes)}"
    )

    print(
        f"Servicios creados: {len(servicios)}"
    )

    print(
        f"Reservas realizadas: {len(reservas)}"
    )

    print(
        "\nSistema finalizado correctamente."
    )