import time
from appUtils import *
from quickSort import *

# @param items - lista de items
# @param W - capacidad máxima de la mochila
# @return beneficio, identificadores de los items elegidos, tiempo de ejecución, y espacio sin usar de la mochila
def solve_greedy(items, W):
    # Para cumplir la opción -t se empieza a contar el tiempo de ejecución
    startTime = time.time()
    # Randomized QuickSort con lambda 
    quickSort(items, lambda x, y: x >= y)
    # Greedy, halla beneficio y rellena taken
    peso_total = valor_total = 0
    taken = [0]*len(items)
    for m in range(len(items)):
        if items[m].weight + peso_total <= W:
            taken[items[m].index] = 1
            valor_total += items[m].value
            peso_total += items[m].weight
    # -r
    espacio = getRoom(W, peso_total)
    # -dt
    identifier = getIdentifier(taken)
    # -t
    elapsedTime = time.time() - startTime
    
    return valor_total, identifier, format(elapsedTime, '.2f'), espacio