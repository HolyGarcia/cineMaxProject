from funtions import mostrar_cartelera
from funtions import mostrar_asientos
from funtions import reservar_asientos
from funtions import cancelar_asientos
from funtions import salir

while True:

    print("")
    print("=" * 15 + "CineMAx -Sistema de Reservas-" + "=" * 15)
    print("")
    print("1. Ver cartelera de un dia")
    print("2. Mostrar asientos de una función")
    print("3. Reservar asientos")
    print("4. Cancelar reserva")
    print("5. Ver disponibilidad")
    print("")
    print("6. Salir")
    print("")



    opcion = int(input("Seleccione un opción: "))

    match opcion:
        case 1:
            mostrar_cartelera.mostrar_cartelera_()
        case 2:
            mostrar_asientos.mostrar_asientos_()
        case 3:
            reservar_asientos.reservar()
        case 4:
            cancelar_asientos.cancelar()
        case 5:
            mostrar_asientos.mostrar_asientos_()
        case 6:
            print("\nGracias por usar CineMax")
            print("Hasta luego!")
            break
    input("\n presione Enter para continuar...")
        
        
    





        
