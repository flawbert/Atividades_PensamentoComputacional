from random import randint
number = randint(1,31)
men = "menor"

modo = int(input("Digite 1- Modo Fácil / 2- Modo Difícil: "))
if modo == 1:
    for i in range(5):
        num = int(input("Escolha um número entre 1 e 31: "))
        men = "Menor" if (num > number) else "Maior"
        if num == number: 
            print("NÚMERO CORRETO!")
            break
        else:
            print(f"Errou! O número correto era: {men}")
if modo == 2:
    for i in range(1):
        num = int(input("Escolha um número entre 1 e 31: "))
        men = "Menor" if (num > number) else "Maior"
        if num == number: 
            print("NÚMERO CORRETO!")
            break
        else:
            print(f"Errou! O número correto era: {men}")

    