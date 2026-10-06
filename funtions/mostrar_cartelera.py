from funtions import mostrar_dias
from datos import datos_cartelera, dias_semana

def mostrar_cartelera_():

    print("")
    print("=" * 15 + "CineMAx -Sistema de Reservas-" + "=" * 15)
    print("")

    mostrar_dias.ver_dia()

    opcion = int(input("Seleccione el dia de la funcion (1-7): "))
    dia = None
    if opcion == 1:
        dia = "Lunes"
    elif opcion == 2:
        dia = "Martes"
    elif opcion == 3:
        dia = "Miércoles"
    elif opcion == 4:
        dia = "Jueves"
    elif opcion == 5:
        dia = "Viernes"
    elif opcion == 6:
        dia = "Sábado"
    elif opcion == 7:
        dia = "Domingo"
    else:
        "Opción no válida, elija un número del (1-7)"
        return

    print(f"\n===== CARTELERA DEL {dia} =====")
    for pelicula in datos_cartelera.cartelera[dia]:
        print(f"\nPelicula: {pelicula["pelicula"]}")
        print(f"Sala: {pelicula["sala"]}")
        print(f"Horario: {pelicula["horario"]}")
        print(f"Formato: {pelicula["formato"]}")

    print("")

    return dia


    




    

