def insertSort(vetor):
    for i in range(1, len(vetor)):
        j = i
        while j > 0 and vetor[j - 1] > vetor[j]:
            vetor[j], vetor[j - 1] = vetor[j - 1], vetor[j]
            j -= 1

a1 = [9, 3, 8, 6, 2]
insertSort(a1)
print(a1)