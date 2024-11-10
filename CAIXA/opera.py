
def saque():
    saqu = int(input("Qual será o valor do saque?"))
    if saqu > saldo:
        print("ERRO! Saque não pode ser superior ao saldo.")
    else:
        arquivo = open('extrato.txt', 'r+')
        hist = arquivo.read()
        arquivo.write(hist + f'- {saqu}\n')

def depo():
    depos = int(input("Qual o valor do depósito?"))
    arquivo = open('extrato.txt', 'r+')
    hist = arquivo.read()
    arquivo.write(hist + f'- {depos}\n')

