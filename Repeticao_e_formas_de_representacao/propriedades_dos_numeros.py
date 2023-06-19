#Múltiplos de 6
numeros = []
n = int(input("Insira um número: "))
print("Múltiplos de 6 menores que o número escolhido: ")
for i in range(1, n+1):
    if i%2 == 0 and i%3 == 0:
        numeros.append(i)
        print(numeros)
print("O múltiplo de 6 após o número escolhido: ")

