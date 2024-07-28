# Faça um programa que leia 5 números e informe o maior número.

maior = float(input("Digite o 1º número: "))

for i in range(2, 6):
    numero = float(input(f"Informe o {i}º numero: "))
    if numero > maior:
        maior = numero

print(f"Dos numeros que voce digitou o maior numero é {maior}")