def verifica_soma(S):
    if S % 2 != 0:
        print("N")

    n = S // 2
    if n % 2 == 0:
        print("SP")
    else:
        print("SI")

S = int(input("Insira o valor de S: "))
resposta = verifica_soma(S)
print(resposta)