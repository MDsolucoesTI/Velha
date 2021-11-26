def imprimeCampo(campo):
	print(" %s | %s | %s " % (campo[0], campo[1], campo[2]))
	print("---|---|---")
	print(" %s | %s | %s " % (campo[3], campo[4], campo[5]))
	print("---|---|---")
	print(" %s | %s | %s " % (campo[6], campo[7], campo[8]))
	
	

def ganhou(simbolo, campo):
	if campo[0] == simbolo and campo[1] == simbolo and campo[2] == simbolo:
		return 1
	if campo[3] == simbolo and campo[4] == simbolo and campo[5] == simbolo:
		return 1
	if campo[6] == simbolo and campo[7] == simbolo and campo[8] == simbolo:
		return 1
	if campo[0] == simbolo and campo[3] == simbolo and campo[6] == simbolo:
		return 1
	if campo[1] == simbolo and campo[4] == simbolo and campo[7] == simbolo:
		return 1
	if campo[2] == simbolo and campo[5] == simbolo and campo[8] == simbolo:
		return 1
	if campo[0] == simbolo and campo[4] == simbolo and campo[8] == simbolo:
		return 1
	if campo[2] == simbolo and campo[4] == simbolo and campo[6] == simbolo:
		return 1

def velha(campo):
	if '-' not in campo:
		return 1

print("------ REGRAS DO JOGO ------")
print("")
print("O primeiro jogador utiliza o simbolo: X")
print("O segundo jogador utiliza o simbolo: O")
print("")
print("Escolha sua jogada através dos números das casas, conforme figura abaixo:")
print("")
print(" 0 | 1 | 2 ")
print("---|---|---")
print(" 3 | 4 | 5 ")
print("---|---|---")
print(" 6 | 7 | 8 ")

resp = input("Vamos jogar? (S ou N)").upper()

if resp == "S":
	campo = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
	
	jogador = 1
	sP1 = 'X'
	sP2 = 'O'
	while 1:
		if velha(campo):
			imprimeCampo(campo)
			print("VELHA")
			break
		if jogador == 1:
			imprimeCampo(campo)
			while 1:
				vc = int(input())
				if campo[vc] == '-':
					break
		
			campo[vc] = sP1
		
			jogador = 2
		
			if ganhou(sP1,campo):
				imprimeCampo(campo)
				print("Jogador 1 GANHOU")
				break
	
		else:
			imprimeCampo(campo)
			while 1:
				vc = int(input())
				if campo[vc] == '-':
					break
		
			campo[vc] = sP2
		
			jogador = 1
		
			if ganhou(sP2,campo):
				imprimeCampo(campo)
				print("Jogador 2 GANHOU")
				break
else:
	print("Obrigado!!!")