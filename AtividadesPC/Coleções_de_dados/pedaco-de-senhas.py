def senha(frase):
    max_frase= ""
    frase_atual = ""

    for char in frase:
        if char not in frase_atual:
            frase_atual += char
        else:
            if len(frase_atual) > len(max_frase):
                max_frase = frase_atual
            frase_atual = char

    if len(frase_atual) > len(max_frase):
        max_frase = frase_atual

    s = max_frase.replace(" ", "")

    return s

frase = input("A sua frase é: ")
s = senha(frase)

if s:
    print("Senha:", s)
else:
    print("ERRO! Não foi possível criar uma senha.")
