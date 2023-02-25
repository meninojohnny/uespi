#JOAO VITOR DA SILVA PEREIRA
#PROBLEMA 1
from sys import stdin

def main():
	while True:
		m = stdin.readline().strip()
		lista = stdin.readline().strip()
		q = stdin.readline().strip()
		if m == '':
			break
		lista2 = lista.split(' ')
		n = False
		b = 1
		g = True if int(lista2[0])%2 == 0 else False
		while True:
			a = 0
			while a != b:
				if len(lista2) == 0:
					break
				if g == True:
					if int(lista2[0])%2 != 0:
						n = True
						break
				else: 
					if int(lista2[0])%2 == 0:
						n = True
						break	
				del lista2[0]
				a += 1
				
			if len(lista2) < (b+1):
				break
			elif n == True:
				break
			else:
				b += 1
			
			a = 0
			while a != b:
				if len(lista2) == 0:
					break
				if g == True:
					if int(lista2[0])%2 == 0:
						n = True
						break
				else: 
					if int(lista2[0])%2 != 0:
						n = True
						break	
				del lista2[0]
				a += 1
				
			if len(lista2) < (b+1):
				break
			elif n == True:
				break
			else:
				b += 1
			
		if n == True:
			print('NAO\n%')
		else:
			print(f'{b}\n%')

if __name__ == '__main__':
	main()
