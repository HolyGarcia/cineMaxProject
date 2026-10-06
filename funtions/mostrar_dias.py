from datos import dias_semana

def ver_dia():
    for n, fila in enumerate(dias_semana.dias, start=1):
            print(f"{n}. {fila}")
    print("")
