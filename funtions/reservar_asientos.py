from datos import Asientos
from funtions import mostrar_cartelera
from funtions import mostrar_asientos


def reservar():

    mostrar_asientos.mostrar_asientos_()

    seleccionar = input("Ingrese los asientos que desea reservar, ej: A1, C3: ")

    seleccionados = seleccionar.upper().split(",")

    for asiento in seleccionados:
        asiento = asiento.strip()

        if len(asiento) !=2:
            print(f"Este '{asiento}' no es valido.")
            return

        letra = asiento[0]
        numero = asiento[1]

        if letra not in ["A", "B", "C", "D", "E"]:
            print(f"La fila '{letra}' no es valida.")
            return

        if numero not in ["1", "2", "3", "4", "5", "6"]:
            print(f"El número '{numero}' no es valido.")
            return

        fila = ord(letra) - ord("A") + 1
        columna = int(numero)

        for asiento in seleccionados:
            asiento = asiento.strip()

            letra = asiento[0]
            numero = asiento[1]

            fila = ord(letra) - ord("A") + 1
            columna = int(numero)

            Asientos.matriz[fila][columna] = "X"

            print("\n========== ASIENTOS ============")
            print("o = Disponibles")
            print("X Reservado\n")

            print("")
            
            print("Reserva realizada correctamente!")
            print("")
            
            for fila in Asientos.matriz:
                print(*fila)
                      
            print("")
        







