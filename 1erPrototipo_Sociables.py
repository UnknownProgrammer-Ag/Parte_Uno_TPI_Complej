from math import sqrt
from time import time
from delta import delta_time


def divisores(entero):
    suma = 1
    div = 2
    cota_sup = sqrt(entero)
    # print(cota_sup, '\n')
    while div <= cota_sup:

        if (entero % div) == 0:
            # print(div, '\n')
            suma += (div+(entero/div))
            # print(suma, '\n')
        div += 1
    return suma

# Tomando el periodo 4, se deben recuperar 4 numeros


def sociables(periodo, numero):
    subconjunto = []
    while periodo > 0:
        if subconjunto != []:
            if numero == subconjunto[0]:
                break
        subconjunto.append(numero)
        numero = divisores(numero)
        periodo -= 1

    if len(subconjunto) < periodo:
        subconjunto = []
    else:
        if numero != subconjunto[0]:
            subconjunto = []
    return subconjunto


@delta_time
def principal():
    conjuntos = []
    for i in range(20000):  # Si prueban con 1300000 va a tardar lo suyo
        social = sociables(5, i)  # Periodo 5 y rango de 20000 tambien sirve
        if social != []:
            conjuntos.append(social)
    if conjuntos == []:
        print("No se encontraron conjuntos")
    else:
        print(conjuntos)


principal()
