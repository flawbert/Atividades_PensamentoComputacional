def extrainumeros(numeros):
    dividendo = numeros[0]
    telefones = []

    for i in range(1, len(numeros)):
        restante = numeros[i] % dividendo
        telefones.append(restante)

    return telefones

numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

numerosextraidos = extrainumeros(numeros)
print("Os telefones são: ")
for numero in numerosextraidos:
    print(numero)
