def encontrasenha(soma_valor, n):
    pares = []

    for i in range(len(n)):
        for x in range(i + 1, len(n)):
            if n[i] + n[x] == soma_valor:
                par = (n[i], n[x])
                pares.append(par)

    if len(pares) == 0:
        return None

    pares.sort()
    senha = f"{pares[0][0]}{pares[0][1]}"
    print(senha)

soma_valor = int(input("Insira a soma: "))
n = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    n.append(numero)

senha = encontrasenha(soma_valor, n)

if senha is not None:
    print("Senha:", senha)
else:
    print("ERRO! Não existe senha para os números inseridos.")
