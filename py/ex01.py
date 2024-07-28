a1 = [34, 65, 23, 7, 9, 13, 52]

for c in range(len(a1)):
    for j in range(c + 1, len(a1)):
        if a1[c] > a1[j]:
        #  troca os numeros de lugar se o primeiro numero for maior que o segundo e assim por diante
         a2 = a1[c]
         a1[c] = a1[j]
         a1[j] = a2

# a variavel C vai percorrer a lista toda
# enquanto j (q é tipo o q o C é pro A1) vai sempre estar a frente de c.
# ai, a gnt verifica se o número na posição C é maior que o numero na posição j.
# se for, a gente troca os dois numeros de lugar usando uma variavel (a2).

print(a1)