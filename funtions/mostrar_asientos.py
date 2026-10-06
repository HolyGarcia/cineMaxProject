from funtions import mostrar_cartelera
from datos import datos_cartelera
from datos import Asientos

def mostrar_asientos_():

    dia = mostrar_cartelera.mostrar_cartelera_()
    opcion = int(input("Seleccione numero de la sala: "))
    sala = opcion

    print(f"\n===== CARTELERA DE LA SALA: {sala} =====")
    for pelicula in datos_cartelera.cartelera[dia]:
        if pelicula["sala"] == sala:
            print(f"\nPelicula: {pelicula["pelicula"]}")
            print(f"Sala: {pelicula["sala"]}")
            print(f"Horario: {pelicula["horario"]}")
            print(f"Formato: {pelicula["formato"]}")
    
    print("")

    Asientos.matriz = Asientos.asientos[dia][sala - 1]

    print("\n========== ASIENTOS ============")
    print("o = Disponibles")
    print("X Reservado\n")

    for fila in Asientos.matriz:
        print(*fila)
          
    print("")





