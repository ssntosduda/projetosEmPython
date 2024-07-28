def insertionSort(algoritmo):
    for i in range(1, len(algoritmo)):
        j = i
        while j > 0 and algoritmo[j -1] > algoritmo[j]:
            algoritmo[j], algoritmo[j - 1] = algoritmo[j - 1], algoritmo[j]
            j -= 1

a1 = [63, 42, 8, 15, 72, 34, 2, 3, 98]
insertionSort(a1)
print(a1)

    