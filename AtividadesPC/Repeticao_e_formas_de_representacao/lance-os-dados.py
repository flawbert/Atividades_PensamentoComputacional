from random import randint

def jogar_dados():
    return  randint(1, 6)

def imprimir_tabuleiro(fabio, isabel, tamanho_tabuleiro):
    print("Tabuleiro:")
    for i in range(tamanho_tabuleiro):
        if fabio == isabel and fabio == i + 1:
            print("Empate", end=" ")
        elif fabio == i + 1:
            print("F", end=" ")
        elif isabel == i + 1:
            print("I", end=" ")
        else:
            print("-", end=" ")
    print()

def jogo():
    tamanho_tabuleiro = int(input("Digite o tamanho do tabuleiro: "))
    fabio = 0
    isabel = 0

    while fabio < tamanho_tabuleiro and isabel < tamanho_tabuleiro:
        input("Fábio, pressione Enter para lançar os dados.")
        lance_fabio = jogar_dados()
        fabio += lance_fabio
        fabio = min(fabio, tamanho_tabuleiro)

        input("Isabel, pressione Enter para lançar os dados.")
        lance_isabel = jogar_dados()
        isabel += lance_isabel
        isabel = min(isabel, tamanho_tabuleiro)

        imprimir_tabuleiro(fabio, isabel, tamanho_tabuleiro)

    if fabio >= tamanho_tabuleiro and isabel >= tamanho_tabuleiro:
        print("Empate!")
    elif fabio >= tamanho_tabuleiro:
        print("Fábio é o vencedor!")
    else:
        print("Isabel é a vencedora!")

if __name__ == '__main__':
    jogo()

