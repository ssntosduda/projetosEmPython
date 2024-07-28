def palindromo(s):
    return s == s[::-1]
# a função compara a str original S com a str invertida[::-1] 
# usando o operador de igualdade(==)

pergunta = str(input("Digite uma palavra: "))

if palindromo(pergunta):
    print('Isso é um palindromo')
else:
    print('Isso não é um palindromo')