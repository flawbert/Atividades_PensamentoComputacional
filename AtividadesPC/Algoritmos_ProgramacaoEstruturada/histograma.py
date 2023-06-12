cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
opcao = int(input("Escolha a opção: 1/Identifica intervalo 2/Calcular frequência de 30 notas: "))
if opcao == 1:
    nota = float(input("Insira uma nota entre 0.0 e 10.0: "))
    if nota == 10.0:
        print("Grupo 4")
    else:
        print(f"Grupo {(nota//2.5) + 1}")

if opcao == 2:
    for i in range(30):
        nota = float(input("Insira uma nota entre 0.0 e 10.0: "))
        if nota >= 0.0 and nota < 2.5:
            cont1 += 1
        elif nota >= 2.5 and nota < 5:
            cont2 += 1
        elif nota >= 5.0 and nota < 7.5:
            cont3 += 1
        elif nota >= 7.5:
            cont4 += 1
    print(f"{cont1} alunos do GRUPO 1")
    print(f"{cont2} alunos do GRUPO 2")
    print(f"{cont3} alunos do GRUPO 3")
    print(f"{cont4} alunos do GRUPO 4")