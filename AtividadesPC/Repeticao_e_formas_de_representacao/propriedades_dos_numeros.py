#Múltiplos de 6
numeros = []
numero = []
n = int(input("Insira um número: "))
print("Múltiplos de 6 menores que o número escolhido: ")
for i in range(1, n+1):
    if i%2 == 0 and i%3 == 0:
        numeros.append(i)
        print(numeros)
print("O múltiplo de 6 após o número escolhido: ")
for i in range(n+1, n+7):
    if i%2 == 0 and i%3 ==0:
        numero.append(i)
        print(numero)
