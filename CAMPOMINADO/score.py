def ver_scores():
    arquivo = open('scores.txt')
    scores = arquivo.readlines()
    print(scores)
    arquivo.close
    scoreNome = str(input("Veja os seus scores: "))
    MeusPontos = scores.get(scoreNome)
    