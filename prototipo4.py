#ALGORITMO PARA HALLAR LOS NUMEROS SOCIALES DE UN PERIODO DADO.

#El concepto de número sociable es la generalización de los conceptos de números amigos y números perfectos. 
# Un conjunto de números sociables es una sucesión alícuota, o una sucesión de números en que cada término es 
# igual a la suma de los factores propios del término anterior. En el caso de los números sociables, la sucesión 
# es cíclica, es decir, los términos se repiten.

#El periodo de esta sucesión, o el orden del conjunto de números sociables, es el número de términos de la 
# sucesión que hay en el ciclo. 

#El usuario podra ingresar el periodo que desea y el rango (cantidad de cifras del numero) donde se desa buscar

from math import sqrt
from delta import delta_time

def descomponer(elemento, cache):
    if elemento in cache:
        return cache[elemento]
    
    sumaDiv = 1  # Sabemos que un numero siempre tendra de divisor a su identidad
    div = 2
    divMax = sqrt(elemento)
    while div <= divMax:
        if (elemento % div) == 0:
            sumaDiv += (div+(elemento//div))
        div += 1
    cache[elemento] = sumaDiv
    return sumaDiv

@delta_time
def sociables():
    periodo = int(input('Ingrese el periodo: '))
    rango = int(input('Ingrese de que rango de numeros desea encontrar los conjuntos sociables existentes: '))
    conjuntos_posibles = set()
    cache = {}
    
    for i in range(rango):
        if i in cache:
            continue
        
        elemento = i
        subconjunto = []
        visitados = set()
        
        while (len(subconjunto) < periodo) and (elemento not in visitados):
            
            visitados.add(elemento)
            subconjunto.append(elemento)
            elemento = descomponer(elemento, cache)
            
            if (int(i) == elemento) and (len(subconjunto) == periodo) and (subconjunto[0] != subconjunto[periodo-1]):
                conjuntos_posibles.add(tuple(subconjunto))
    
    if conjuntos_posibles:
        print('Para ', rango, ' numeros, existen estos conjuntos de periodo ', periodo, ':', conjuntos_posibles)


sociables()