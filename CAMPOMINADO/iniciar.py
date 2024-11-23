from score import ver_scores
from jogo import jogo 
from jogo import criarminas
from jogo import escolher

def main():
    while True:
        print("\nCampo Minado 2024")
        print("1 - JOGAR")
        print("2 - VER SCORES")
        print("3 - SAIR")
        
        try:
            menu = int(input("Escolha uma opção (1-3): "))
        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue
        
        if menu == 1:
            nome = input("Digite seu nome: ")
            tabuleiro = jogo()
            minas = criarminas()
            escolher(nome, tabuleiro, minas)
        elif menu == 2:
            ver_scores()
        elif menu == 3:
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
