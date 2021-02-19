import random

# @param array
# @param inDesiredOrder - orden, de mayor a menor, o de menor a mayor
def quickSort(array, inDesiredOrder):

    # @param array
    # @param start - índice en el que se desea empezar a realizar la ordenación
    # @param stop - índice en el que se desea parar de realizar la ordenación
    # @param inDesiredOrder - orden, de mayor a menor, o de menor a mayor
    def _quickSort(array, start, stop, inDesiredOrder):
        if start < stop:
            pivotIndex = partitionRand(array, start, stop, inDesiredOrder)
            _quickSort(array, start, pivotIndex-1, inDesiredOrder)
            _quickSort(array, pivotIndex+1, stop, inDesiredOrder)

    # @param array
    # @param start - índice en el que se desea empezar a realizar la ordenación
    # @param stop - índice en el que se desea parar de realizar la ordenación
    # @param inDesiredOrder - orden, de mayor a menor, o de menor a mayor
    # @return índice de pivote
    def partitionRand(array, start, stop, inDesiredOrder):
        randPivot = random.randrange(start, stop)
        array[start], array[randPivot] = array[randPivot], array[start]
        return partition(array, start, stop, inDesiredOrder)

    # @param array
    # @param start - índice en el que se desea empezar a realizar la ordenación
    # @param stop - índice en el que se desea parar de realizar la ordenación
    # @param inDesiredOrder - orden, de mayor a menor, o de menor a mayor
    # @return índice de pivote
    def partition(array, start, stop, inDesiredOrder):
        pivot = start
        i = start + 1

        for j in range(start + 1, stop + 1):
            if inDesiredOrder(array[j].value, array[pivot].value):
                array[i], array[j] = array[j], array[i]
                i += 1

        array[pivot], array[i - 1] = array[i - 1], array[pivot]
        pivot = i - 1
        return pivot

    _quickSort(array, 0, len(array)-1, inDesiredOrder)