from funtions import mostrar_asientos
from datos import Asientos

def cancelar():

    mostrar_asientos.mostrar_asientos_()

    seleccionar = input("Ingrese los asientos que desea cancelar, ej: A1, C3: ")

    seleccionados = seleccionar.upper().split(",")

    validar = False

    for asiento in seleccionados:
        asiento = asiento.strip()

        letra = asiento[0]
        numero = asiento[1]

        fila = ord(letra) - ord("A") + 1
        columna = int(numero)

        if Asientos.matriz[fila][columna] != "X":
            print(f"El número '{numero}' no está reservado.")
            return

    for asiento in seleccionados:
        asiento = asiento.strip()

        letra = asiento[0]
        numero = asiento[1]

        fila = ord(letra) - ord("A")+1
        columna = int(numero)

        Asientos.matriz[fila][columna] = "o"

    print("")

    print("Reserva cancelada correctamente!")
    print("")

    for fila in Asientos.matriz:
        print(*fila)
    print("")








    



    