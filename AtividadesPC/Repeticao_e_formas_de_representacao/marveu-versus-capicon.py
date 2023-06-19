import statistics

def encontrar_minimo(numeros):
    return min(numeros)

def encontrar_maximo(numeros):
    return max(numeros)

def encontrar_argumento_minimo(numeros):
    minimo = min(numeros)
    for i, num in enumerate(numeros):
        if num == minimo:
            return i + 1

def encontrar_argumento_maximo(numeros):
    maximo = max(numeros)
    for i, num in enumerate(numeros):
        if num == maximo:
            return i + 1

def calcular_somatorio(numeros):
    return sum(numeros)

def calcular_produtor(numeros):
    produtor = 1
    for num in numeros:
        produtor *= num
    return produtor

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    return statistics.median(numeros)

def verificar_todos_primos(numeros):
    for num in numeros:
        if not eh_primo(num):
            return False
    return True

def verificar_algum_primo(numeros):
    for num in numeros:
        if eh_primo(num):
            return True
    return False

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Exemplo de uso das funções
numeros = []

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

# Desafio: Mínimo e máximo
minimo = encontrar_minimo(numeros)
maximo = encontrar_maximo(numeros)
print("Mínimo:", minimo)
print("Máximo:", maximo)

# Desafio: Argumentos mínimo e máximo
argumento_minimo = encontrar_argumento_minimo(numeros)
argumento_maximo = encontrar_argumento_maximo(numeros)
print("Argumento mínimo:", argumento_minimo)
print("Argumento máximo:", argumento_maximo)

# Desafio: Somatório e produtor
somatorio = calcular_somatorio(numeros)
produtor = calcular_produtor(numeros)
print("Somatório:", somatorio)
print("Produtor:", produtor)

# Desafio: Média e mediana
media = calcular_media(numeros)
mediana = calcular_mediana(numeros)
print("Média:", media)
print("Mediana:", mediana)

# Desafio: Todos e algum
todos_primos = verificar_todos_primos(numeros)
algum_primo = verificar_algum_primo(numeros)
print("Todos os números são primos?", todos_primos)
print("Algum número é primo?", algum_primo)