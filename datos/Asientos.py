from datos import dias_semana
 
asientos_valor = [
    [" ", "1", "2", "3", "4", "5", "6"],
    ["A", "o", "o", "o", "o", "o", "o"],
    ["B", "o", "o", "o", "o", "o", "o"],
    ["C", "o", "o", "o", "o", "o", "o"],
    ["D", "o", "o", "o", "o", "o", "o"],
    ["E", "o", "o", "o", "o", "o", "o"]
]

asientos = {}

for dia in dias_semana.dias:
    asientos[dia] = []

    for funcion in range(5):
        matriz = []

        for fila in asientos_valor:
            matriz.append(fila.copy())

        asientos[dia].append(matriz)


