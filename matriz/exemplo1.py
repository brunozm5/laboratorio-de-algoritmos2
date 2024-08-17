def multiplicar_matriz(matriz_informada, numero_escalar):
    for linha in range(len(matriz_informada)):
        for coluna in range(len(matriz_informada[linha])):
            matriz_informada[linha][coluna] = matriz_informada[linha][coluna] * numero_escalar

    return matriz_informada

matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna], end="\t")
    print("")
        