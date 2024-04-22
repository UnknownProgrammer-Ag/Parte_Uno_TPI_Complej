from math import sqrt
from time import time
from delta import delta_time


@delta_time
def sociables():
    periodo = input('Ingrese el periodo')
    rango = input(
        'Ingrese de que rango de numeros desea encontrar los conjuntos sociables existentes')
    conjuntos_posibles = set()
    subconjunto = set()

    for i in range(rango):

        # REFORMAR ESTA IDEA REDUCIENDO LA COMPLEJIDAD
        elemento=i
        while len(subconjunto) < periodo:
            sumaDiv=1 #Sabemos que un numero siempre tendra de divisor a su identidad
            div=2 
            divMax=sqrt(elemento) 
            while div <= divMax:
                if (elemento % div) == 0:
                    sumaDiv += (div+(elemento/div))
                div += 1


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

    social = sociables(5, i)  # Periodo 5 y rango de 20000 tambien sirve
    if social != []:
        conjuntos.append(social)
    if conjuntos == []:
        print("No se encontraron conjuntos")
    else:
        print(conjuntos)
# x.add( < elem > )
# x.remove( < elem > )
# x.discard( < elem > )
# x.clear()
