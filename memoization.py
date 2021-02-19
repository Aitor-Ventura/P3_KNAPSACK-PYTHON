import numpy as np
import time
from appUtils import *

# @param items - lista de items
# @param capacity - capacidad máxima de la mochila
# @return beneficio, identificadores de los items elegidos, tiempo de ejecución, y espacio sin usar de la mochila
def solve_memoization(items, capacity):
    # @param items - lista de items
    # @param m - matriz de elementos
    # @param n - longitud de la lista de items
    # @param capacity - capacidad máxima de la mochila
    # @return beneficio
    def knapsack_helper(items, m, n, capacity):
        if m[n-1, capacity] >= 0: return m[n-1, capacity]

        if n == 0: benefit = 0
        elif items[n-1].weight <= capacity:
            benefit = max(knapsack_helper(items, m, n - 1, capacity - items[n-1].weight) + items[n-1].value,
                    knapsack_helper(items, m, n - 1, capacity))
        else: benefit = knapsack_helper(items, m, n - 1, capacity)

        m[n-1, capacity] = benefit
        return benefit
    
    # @param matrix - matriz de elementos
    # @param items - lista de items
    # @return lista de elementos escogidos
    def encuentra(matrix, items):
        taken = [0]*len(items)
        i, j = len(matrix) - 1, len(matrix[0]) - 1
        while i > 0:
            if matrix[i][j] != matrix[i-1][j]:
                taken[i] = 1
                j -= items[i].weight
            i -= 1
        return taken
    
    # Para cumplir la opción -t se empieza a contar el tiempo de ejecución
    startTime = time.time()

    n = len(items)
    m = np.full((n, capacity + 1), -1)
    benefit = knapsack_helper(items, m, n, capacity)
    taken = encuentra(m, items)
    # -t
    elapsedTime = time.time() - startTime
    peso_total = getTotalWeight(items, taken)
    # -r
    espacio = getRoom(capacity, peso_total)
    # -dt
    identifier = getIdentifier(taken)

    return benefit, identifier, format(elapsedTime, '.2f'), espacio