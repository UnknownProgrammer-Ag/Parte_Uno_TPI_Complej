from decorators import delta_time

def descomponer(elemento, cache, primos):
    if elemento in cache:
        return cache[elemento]
    
    cont = 0
    sumaDiv = 1
    div = 2
    divMax = (elemento)**(0.5)
    while div <= divMax:
        if (elemento % div) == 0:
            sumaDiv += (div+(elemento//divMax))
            cont += 1
        div += 1
    if cont >= 4:
        cache[elemento] = sumaDiv
    if sumaDiv == 1:
        primos[elemento] = 1
    return sumaDiv

@delta_time  # "Grupo G1"
def sociables(N, PERIODOS):
    for periodo in PERIODOS:
        lista = set()
        cache = {}
        primos = {}
        for i in range(N):
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
                lista.add(tuple(sorted(subconjunto)))

        print(lista)

if __name__ == "__main__":
    # INGRESO DATOS
    print(sociables(100000, [5, 6, 7]))
