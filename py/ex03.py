maior = None
#  é um valor especial em Python que representa a ausencia de um valor.

for _ in range(5):
    n = float(input("Digite um número: "))
    if maior is None or n > maior:
        maior = n

# maior is None: isso pe verdadeiro se a variavel maior ainda nao foi atribuida a nenhum numero 
# (ja que inicia em None).
# n > maior: isso é verdadeiro se o numero atual (n) for maior que o valor atual de maior.

print("O maior número é: ", maior)