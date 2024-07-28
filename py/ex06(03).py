def insertionSort(algoritmo):
    for i in range(1, len(algoritmo)):
        j = i
        while j > 0 and algoritmo[j -1] > algoritmo[j]:
            algoritmo[j], algoritmo[j - 1] = algoritmo[j - 1], algoritmo[j]
            j -= 1

def insertionSortReverse(algoritmo):
    for i in range(1, len(algoritmo)):
        j = i
        while j < 0 and algoritmo[j -1] < algoritmo[j]:
            algoritmo[j], algoritmo[j - 1] = algoritmo[j - 1], algoritmo[j]
            j -= 1

impares = []
pares = []
a1 = [10, 4, 32, 543, 3456, 654, 567, 87, 6789, 98]
for i in a1:
    if i %2 == 0:
        pares.append(i)
    else: 
        impares.append(i)

insertionSort(a1)
print(a1)

    