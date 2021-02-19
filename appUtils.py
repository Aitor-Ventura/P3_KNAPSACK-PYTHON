from collections import namedtuple
import sys

# Definición de Item, una lista anidada que está categorizada por índice, valor, y peso
Item = namedtuple("Item", ['index', 'value', 'weight'])

# @param items - lista de items
# @param taken - lista de elementos escogidos
# @return peso total de los items escogidos
def getTotalWeight(items, taken):
    weight = 0
    for m in range(len(taken)):
        if taken[m] == 1: weight += items[m].weight
    return weight

# @param W - capacidad de la mochila
# @param peso_total - peso de los items dentro de la mochila
# @return peso sobrante de la mochila
def getRoom(W, peso_total): return W - peso_total

# @param taken - lista de elementos escogidos
# @return lista con el identificador de los elementos escogidos
def getIdentifier(taken):
    res = []
    for m in range(len(taken)): 
        if taken[m] == 1: res.append(m)
    return res

# @param input - fichero único que es procesado
# @return lista de items, capacidad máxima de la mochila
def fromDataToItems(input):
    fich = open(input, "r")
    cont = fich.read()
    lines = cont.split('\n')
    first_line = lines[0].split()
    item_count = int(first_line[0])
    capacity = int(first_line[1])

    items = []
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
    
    return items, capacity

# Muestra el mensaje de ayuda y sale del programa
def displayHelp():
      print("""usage: main.py [-h] [-d [DIRECTORY] | -f [FILE]] [-b] [-r] [-t] [-dt] [-sg | -sm | -st]

      optional arguments:
            -h, --help                                show this help message and exit
            -d [DIRECTORY], --directory [DIRECTORY]   process many files in a directory
            -f [FILE], --file [FILE]                  process a single file
            -b, --benefit                             display benefit
            -r, --room                                display unused knapsack weight
            -t, --time                                display execution time
            -dt, --display_taken                      display identifier of taken items
            -sg, --greedy                             solve the knapsack 01 problem with Greedy
            -st, --tabulation                         solve the knapsack 01 problem with Tabulation
            -sm, --memoization                        solve the knapsack 01 problem with Memoization """)
      sys.exit()

# Devuelve verdadero si se pide mostrar el beneficio por pantalla, falso si no
def benefit(argv): return "-b" in argv or "--benefit" in argv

# Devuelve verdadero si se pide mostrar los identificadores de los items por pantalla, falso si no
def display_taken(argv): return "-dt" in argv or "--display_taken" in argv

# Devuelve verdadero si se pide mostrar el peso sobrante de la mochila, falso si no
def room(argv): return "-r" in argv or "--room" in argv

# Devuelve verdadero si se pide mostrar el tiempo de ejecución por pantalla, falso si no
def displayTime(argv): return "-t" in argv or "--time" in argv