def insertionSort(vetor):
    for i in range(len(vetor)):
        for j in range(i + 1, len(vetor)):
            # vetor[i], vetor[i-1] = vetor[i-1], vetor[i]
            print(f'{vetor} \n')
            print(f'Vamos comparar {a1[i]} com {a1[j]} \n')
            while a1[i] > a1[j]:
                print(f'Vamos trocar {a1[i]} por {a1[j]} \n')
                a2 = a1[i]
                a1[i] = a1[j]
                a1[j] = a2
a1 = [9, 3, 8, 6, 2]
insertionSort(a1)
print(a1)
