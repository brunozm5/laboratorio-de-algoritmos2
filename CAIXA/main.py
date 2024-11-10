# O sistema de caixa eletrônico deve apresentar as seguintes funcionalidades:

# 	Sacar: Permite ao usuário retirar um valor, desde que haja saldo suficiente.
# 	Depositar: Permite ao usuário adicionar um valor à conta.
# 	Consultar Saldo: Mostra o saldo atual do usuário.
# 	Ver Extrato: Exibe o histórico das transações realizadas.
# 	Sair: Encerra o sistema.

import saque from opera
import depo from opera

def main():
	saldo = int(input("Insira o saldo atual: "))
	opçao = int(input(f"Selecione uma opção\n 1. Sacar\n 2. Depositar\n 3. Consultar saldo\n 4. Ver extrato\n 5. Sair\n Opção: "))
	if opçao == 1:
		saque()
		saldo = saldo - saqu
		opçao = int(input(f"Selecione uma opção\n 1. Sacar\n 2. Depositar\n 3. Consultar saldo\n 4. Ver extrato\n 5. Sair\n Opção: "))
	elif opçao == 2:
		depo()
		saldo = saldo + depos
    	opçao = int(input(f"Selecione uma opção\n 1. Sacar\n 2. Depositar\n 3. Consultar saldo\n 4. Ver extrato\n 5. Sair\n Opção: "))
	elif opçao == 3:
	    print("Seu saldo atual é de R$ ", saldo)
	elif opçao == 4:
	    arquivo = open('extrato.txt', 'r')
        print(arquivo.readline())
	elif opçao == 5:
	    "Até logo!"
		break