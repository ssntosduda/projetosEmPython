def insertionSort(p1):
    for i in range(len(p1)):
        j = i
        while j > 0 and len(p1[j -1]) > len(p1[j]):
            p1[j], p1[j - 1] = p1[j - 1], p1[j]
            j -= 1

a1 = ["anteontem", "amanha", "duda"]
insertionSort(a1)
print(a1)
                