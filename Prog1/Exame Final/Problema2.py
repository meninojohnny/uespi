"""
Exemplo de entrada:
5 10 ----- Numero de partidas
 '---------- - Numero de jogadores
"""
from sys import stdin
def main():	
	import random
	n = stdin.readline().split(" ")
	a, b = n
	a = int(a)
	b = int(b)
	jog = ['']* a
	pontos = [0]* a
	x = ('Pedra', 'Tesoura', 'Papel')
	partidas = 0
	for i in range(0, b):
		venc = []
	
		jog2 = jog[:]
		while True:
			for c in range(0, a):
				e = random.choices(x)
				if e == ['Pedra'] and jog2[c] == e:
					while e == ['Pedra']:
						e = random.choices(x)
				jog[c] = e
			if jog.count(jog[0]) != a:
				break
				
		if jog.count(['Pedra']) == 0:
			for d in range(0, a):
				if jog[d] == ['Tesoura']:
					pontos[d] += 1
					venc.append('Jogador ' + str((d + 1)))
								
		elif jog.count(['Tesoura']) == 0:
			for f in range(0, a):
				if jog[f] == ['Papel']:
					pontos[f] += 1
					venc.append('Jogador ' + str(f+1))
		elif jog.count(['Pedra']) > 0:
			for j in range(0, a):
				if jog[j] == ['Pedra']:
					pontos[j] += 1
					venc.append('Jogador' + str(j+1))
		
		print('----------------------------------')	
		print(f'PARTIDA: {i + 1}')		
		for i in range(0, a):
			print(f'JOGADOR {i + 1}: {jog[i][0]}')
		print(f'VENCEDORES: {venc}')
	
	print('----------------------------------')
	print('------ RESUMO DAS PARTIDAS -------')	
	for i in range(0, a):
		print(f'JOGADOR {i + 1}: ganhou {pontos[i]} partida(s)')
	print('----------------------------------')
if __name__ == '__main__':
	main()
