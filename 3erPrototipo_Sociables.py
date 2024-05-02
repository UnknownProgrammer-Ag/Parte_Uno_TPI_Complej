from math import sqrt
from delta import delta_time


@delta_time
def sociables():
    periodo = int(input('Ingrese el periodo '))
    rango = int(input(
        'Ingrese de que rango de numeros desea encontrar los conjuntos sociables existentes '))
    conjuntos_posibles = set()
    for i in range(rango):
        elemento = i
        subconjunto = []
        while (len(subconjunto) < periodo):
            sumaDiv = 1  # Sabemos que un numero siempre tendra de divisor a su identidad
            div = 2
            divMax = sqrt(elemento)
            while div <= divMax:
                if (elemento % div) == 0:
                    sumaDiv += (div+(elemento//div))
                div += 1
            # Ver alguna forma de verificar que los conjuntos no sean nros amigos repetidos en periodo para
            subconjunto.append(elemento)
            elemento = sumaDiv
        if (int(i) == elemento) and (len(subconjunto) == periodo) and (subconjunto[0] != subconjunto[periodo-1]):
            conjuntos_posibles.add(tuple(subconjunto))
    if conjuntos_posibles:
        print('Para ', rango, ' numeros, existen estos conjuntos de periodo ',
              periodo, ' :', conjuntos_posibles)


sociables()
