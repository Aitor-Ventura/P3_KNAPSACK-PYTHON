from appUtils import *
from greedy import *
from tabulation import *
from memoization import *
import sys, os, re

# Variables globales, control de argumentos
argv = sys.argv
#argc = len(sys.argv)
grF = tbF = mmF = False

# @param data - directorio
# @return lista de elementos de un fichero ordenados alfanuméricamente 
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)


# Printa por pantalla según las opciones elegidas en línea de comandos
def printOptions():
      if benefit(argv): print(str(int(beneficio)), end="\t")
      if display_taken(argv): print(str(data), end="\t")
      if room(argv): print(str(espacio), end="kg\t")
      if displayTime(argv): print(str(tiempo), end="s\t")
      print("\n")

# Si se encuentra -h en la lista de argumentos, mostrar el mensaje de ayuda y salir del programa
if "-h" in argv or "--help" in argv: displayHelp()

# Orden de priorización: greedy > tabulation > memoization. Solo se puede elegir uno
if "-sg" in argv or "--greedy" in argv: grF, tbF, mmF = True, False, False
elif "-st" in argv or "--tabulation" in argv: grF, tbF, mmF = False, True, False
elif "-sm" in argv or "--memoization" in argv: grF, tbF, mmF = False, False, True

# Procesar el argumento que se encuentra después de donde se sitúa -d o --directory
flag, input = False, None

if "-d" in argv: flag, input = True, argv[argv.index("-d")+1]
elif "--directory" in argv: flag, input = True, argv[argv.index("--directory")+1]

# Ordenar alfanuméricamente los ficheros del directorio pasado por parámetro
if flag: cont = sorted_alphanumeric(os.listdir(input))
      
# Procesar el argumento que se encuentra después de donde se sitúa -f o --file
else:
      if "-f" in argv: input = argv[argv.index("-f")+1]
      elif "--file" in argv: input = argv[argv.index("--file")+1]
      items, capacity = fromDataToItems(input)

# Directory
if flag:
      # Greedy
      if grF:
            for fich in cont:
                  items, capacity = fromDataToItems(input + "/" + fich)
                  greedy = items.copy()
                  beneficio, data, tiempo, espacio = solve_greedy(greedy, capacity)
                  print("Greedy: ", fich, end="\t")
                  printOptions()
      # Tabulation
      elif tbF:
            for fich in cont:
                  items, capacity = fromDataToItems(input + "/" + fich)
                  tabulation = items.copy()
                  beneficio, data, tiempo, espacio = solve_tabulation(tabulation, capacity)
                  print("Tabulation: ", fich, end="\t")
                  printOptions()
      # Memoization
      elif mmF:
            for fich in cont:
                  items, capacity = fromDataToItems(input + "/" + fich)
                  memoization = items.copy()
                  beneficio, data, tiempo, espacio = solve_memoization(memoization, capacity)
                  print("Memoization: ", fich, end="\t")
                  printOptions()
# Single file
else:
      # Greedy
      if grF:
            greedy = items.copy()
            beneficio, data, tiempo, espacio = solve_greedy(greedy, capacity)
            print("Greedy: ", input, end="\t")
            printOptions()
      # Tabulation
      elif tbF:
            tabulation = items.copy()
            beneficio, data, tiempo, espacio = solve_tabulation(tabulation, capacity)
            print("Tabulation: ", input, end="\t")
            printOptions()
      # Memoization
      elif mmF:
            memoization = items.copy()
            beneficio, data, tiempo, espacio = solve_memoization(memoization, capacity)
            print("Memoization: ", input, end="\t")
            printOptions()