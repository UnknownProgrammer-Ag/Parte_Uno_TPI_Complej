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
        subconjunto = set()
        bucle = periodo
        while (len(subconjunto) < periodo) and (bucle > 0):
            sumaDiv = 1  # Sabemos que un numero siempre tendra de divisor a su identidad
            div = 2
            divMax = sqrt(elemento)
            while div <= divMax:
                if (elemento % div) == 0:
                    sumaDiv += (div+(elemento//div))
                div += 1
            subconjunto.add(elemento)
            elemento = sumaDiv
            bucle -= 1
        if (int(i) == elemento):
            conjuntos_posibles.add(frozenset(subconjunto))

    if bool(conjuntos_posibles):
        print('Para ', rango, ' numeros, existen estos conjuntos de periodo ',
              periodo, ' :', [i for i in conjuntos_posibles if (len(i) == periodo)])
    else:
        print('No se encontraron conjuntos')


sociables()
