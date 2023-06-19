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
#------------------------------------------------------------

#Primo ou Composto
def verificar_primalidade(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True 
n = int(input("Insira um número: "))
if verificar_primalidade(n):
    print(n, "é um número primo.")
elif n < 2:
  print("Números menores do que 2 não são primos! ")
else:
    print(n, "é um número composto.")
         
