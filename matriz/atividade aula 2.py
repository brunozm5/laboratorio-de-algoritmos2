#1
def multiplicar_matriz(matriz_informada, numero_escalar):
    for linha in range(len(matriz_informada)):
        for coluna in range(len(matriz_informada[linha])):
            matriz_informada[linha][coluna] = matriz_informada[linha][coluna] * numero_escalar


#2
def buscar_valor_em_matriz(matriz, valor):
    numero_existe = False
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == valor:
                numero_existe = True
    if numero_existe:
        print("Número está presente na matriz.")
    else:
        print("Número não está presente na matriz.")


#3
def menor_valor_na_matriz(matriz):
    return min(min(linha) for linha in matriz)

#4
def soma_dos_valores_da_matriz(matriz):
    return sum(sum(linha) for linha in matriz)