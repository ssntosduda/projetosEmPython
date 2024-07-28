def insertSort(vetor):
    for i in range(1, len(vetor)):
        valAval = vetor[i]
        if valAval < vetor[i -1]:
            vetor[i], vetor[i-1] = vetor[i-1], vetor[i]
            print(vetor)
        else: 
            print("Não trocou!!")

a1 = [3, 2]
insertSort(a1)
print(a1)