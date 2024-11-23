import random
import os

LINHAS = 7
COLUNAS = 7
MINAS = 20

def jogo():
    tabuleiro = [['⬜' for _ in range(COLUNAS)] for _ in range(LINHAS)]
    return tabuleiro

def criarminas():
    minas = set()
    while len(minas) < MINAS:
        linha = random.randint(0, LINHAS - 1)
        coluna = random.randint(0, COLUNAS - 1)
        minas.add((linha, coluna))
    return minas

def contarminas(linha, coluna, minas):
    contagem = 0
    for i in range(linha - 1, linha + 2):
        for j in range(coluna - 1, coluna + 2):
            if 0 <= i < LINHAS and 0 <= j < COLUNAS and (i, j) in minas:
                contagem += 1
    return contagem

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

def escolher(nome, tabuleiro, minas):
    fim = False
    score = 50  
    while not fim:
        mostrar_tabuleiro(tabuleiro)
        X = int(input("Escolha a posição horizontal (0 - 6): "))
        Y = int(input("Escolha a posição vertical (0 - 6): "))
        score -= 1
        if (X, Y) in minas:
            fim = True
            tabuleiro[X][Y] = '💣' 
            print("Você encontrou uma mina! Fim de jogo!")
        else:
            minas_ao_redor = contarminas(X, Y, minas)
            tabuleiro[X][Y] = str(minas_ao_redor)  
            if all(tabuleiro[i][j] != '⬜' for i in range(LINHAS) for j in range(COLUNAS) if (i, j) not in minas):
                fim = True
                print(f"Parabéns {nome}, você venceu o jogo com {score} pontos!")
                dici = {'nome': nome, 'score': score}
                arquivo = open('scores.txt', 'a')
                arquivo.write(f"{dici}\n")
                arquivo.close
