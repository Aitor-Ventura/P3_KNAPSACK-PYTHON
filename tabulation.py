import numpy as np
import time
from appUtils import *

# @param items - lista de items
# @param capacity - capacidad máxima de la mochila
# @return beneficio, identificadores de los items elegidos, tiempo de ejecución, y espacio sin usar de la mochila
def solve_tabulation(items, capacity):
    # Para cumplir la opción -t se empieza a contar el tiempo de ejecución
    startTime = time.time()

    n = len(items)
    W = capacity
    benefit = np.zeros((n, W + 1))
    # Beneficio
    for i in range(1, n):
        for j in range(1, W + 1):
            if items[i].weight <= j:
                if items[i].value + benefit[i - 1, j - items[i].weight] > benefit[i - 1, j]:
                    benefit[i, j] = items[i].value + benefit[i - 1, j - items[i].weight]
                else: benefit[i, j] = benefit[i - 1, j]
            else: benefit[i, j] = benefit[i - 1, j]
    # Rellenar taken
    taken = [0]*len(items)
    i, k = n - 1, W
    while i > 0 and k > 0:
        if benefit[i, k] != benefit[i - 1, k]: taken[i], k = 1, k - items[i].weight
        else: i = i - 1
    # -t
    elapsedTime = time.time() - startTime
    # -r
    peso_total = getTotalWeight(items, taken)
    espacio = getRoom(W, peso_total)
    # -dt
    identifier = getIdentifier(taken)

    return benefit[n - 1, W], identifier, format(elapsedTime, '.2f'), espacio