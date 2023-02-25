#JOAO VITOR DA SILVA PEREIRA
#PROBLEMA 2
from sys import stdin

def main():
	t, p = stdin.readline().strip().split(' ')
	
	a = []
	for i in range(1, int(t)+1):
		a.append([])
	
	while True:
		linha = stdin.readline().strip().split(' ')
		if linha == ['']:
			break
		else:
			ind, dir = linha
			a[int(ind)-1] = [int(dir)]
			
	a1 = a[:]
	a2 = a[:]
		
	b = 0
	for i in a:
		if i == [1]:
			a1[b] = i
		elif i == [-1]:
			a2[b] = i
		b += 1
			
	b = 0
	for i in a1:
		if i == []:
			a1[b] = ['A']
		b += 1
		
	b = 0	
	for i in a2:
		if i == []:
			a2[b] = ['A']
		b += 1
		
	b = 0
	for i in a:
		if i == []:
			a1[b] = []
			a2[b] = []
		b += 1
				
	b = 0	
	espa1 = []	
	for i in a:
		if i == []:
			espa1.append(b)
		b += 1
				
	cont = 0
	while True:
		cont += 1
			
		a1.insert(0, a1[-1])
		del a1[-1]
		
		
		a2.append(a2[0])
		del a2[0]
			
			
		espa2 = []
		espa3 = []
		b = 0
		for i in a1:
			if i == []:
				espa2.append(b)
			b += 1
				
		b = 0
		for i in a2:
			if i == []:
				espa3.append(b)
			b += 1
			
		if espa1 == espa2 and espa1 == espa3:
			break
				
	print(cont)
			
if __name__ == '__main__':
	main()
