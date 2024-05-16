from decorators import delta_time


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


@delta_time("GRUPO G1")
def sociables(N, periodos):
    lista = []
    for periodo in periodos:

        conjuntos_posibles = set()
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
                conjuntos_posibles.add(tuple(sorted(subconjunto)))

        if conjuntos_posibles:
            # print('Para', rango, 'numeros, existen estos conjuntos de periodo',
            # 	periodo, ':', conjuntos_posibles)
            lista.append(conjuntos_posibles)

    return lista


if __name__ == "__main__":
    # INGRESO DATOS
    print(sociables(N, periodos))
