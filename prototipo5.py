# ALGORITMO PARA HALLAR LOS NUMEROS SOCIALES DE UN PERIODO DADO.

# El concepto de número sociable es la generalización de los conceptos de números amigos y números perfectos.
# Un conjunto de números sociables es una sucesión alícuota, o una sucesión de números en que cada término es
# igual a la suma de los factores propios del término anterior. En el caso de los números sociables, la sucesión
# es cíclica, es decir, los términos se repiten.

# El periodo de esta sucesión, o el orden del conjunto de números sociables, es el número de términos de la
# sucesión que hay en el ciclo.

# El usuario podra ingresar el periodo que desea y el rango (cantidad de cifras del numero) donde se desa buscar

from delta import delta_time

def descomponer(elemento, cache, primos):
    if elemento in cache:
        return cache[elemento]
    
    cont = 0
    sumaDiv = 1  # Sabemos que un numero siempre tendra de divisor a su identidad
    div = 2
    divMax = (elemento)**(0.5)
    while div <= divMax:
        if (elemento % div) == 0:
            sumaDiv += (div+(elemento//div))
            cont += 1
        div += 1
    
    if cont >= 4:
        cache[elemento] = sumaDiv
    if sumaDiv == 1:
        primos[elemento] = 1
    
    return sumaDiv


@delta_time
def sociables(rango, periodo):
    
    conjuntos_posibles = set()
    cache = {}
    primos = {}

    for i in range(rango):
        if i in cache or i in primos:
            continue

        elemento = i
        subconjunto = []
        visitados = set()

        while (len(subconjunto) < periodo) and (elemento not in visitados):

            visitados.add(elemento)
            subconjunto.append(elemento)
            if elemento in primos:
                continue
            elemento = descomponer(elemento, cache, primos)

        if (i == elemento) and (len(visitados) == periodo) and (subconjunto[0] != subconjunto[periodo-1]):
            conjuntos_posibles.add(tuple(sorted(subconjunto)))

    if conjuntos_posibles:
        print('Para', rango, 'numeros, existen estos conjuntos de periodo',
              periodo, ':', conjuntos_posibles)


def preguntar():
    periodo = int(input('Ingrese el periodo: '))
    rango = int(input('Ingrese de que rango de numeros desea encontrar los conjuntos sociables existentes: '))
    
    sociables(rango, periodo)


preguntar()


# Pasos que sigue el algoritmo para finalizar exitosamente
# 1. Almacena periodo y rango
# 1.1. Periodo es la cantidad de numeros sociables a encontrar
# 1.2. Rango es el valor maximo de numeros en los que encontrará el primer número sociable.
# 2. 