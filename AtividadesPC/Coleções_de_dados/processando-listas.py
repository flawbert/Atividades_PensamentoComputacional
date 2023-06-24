dados = [16, 69, 85, 15, 8, 3, 2, 94, 35, 4]


minimo = min(dados)
maximo = max(dados)
print("Mínimo (Márveu):", minimo)  
print("Máximo (Cápicon):", maximo)  


indice_minimo = dados.index(minimo) + 1
indice_maximo = dados.index(maximo) + 1
print("Mínimo encontrado no elemento (Márveu)", indice_minimo)  
print("Máximo encontrado no elemento (Cápicon)", indice_maximo) 


soma = sum(dados)
produto = 1
for num in dados:
    produto *= num
print("Somatório (Márveu):", soma)
print("Produtório (Cápicon):", produto)


media = sum(dados) / len(dados)
dados_ordenados = sorted(dados)
mediana = dados_ordenados[len(dados_ordenados) // 2]
print("Média (Márveu):", media)
print("Mediana (Cápicon):", mediana)


def is_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

todos_primos = all(is_primo(num) for num in dados)
algum_primo = any(is_primo(num) for num in dados)
print("Todos os números são primos?", todos_primos)  # Márveu
print("Algum número é primo?", algum_primo)