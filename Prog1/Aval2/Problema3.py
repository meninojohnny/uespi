#JOÃO VITOR DA SILVA PEREIRA
#PROBLEMA 3
from sys import stdin

def main():
	while True: 
		palavra = stdin.readline().strip()
		if palavra == '':
			break
			
		p7 = (('am', 'aim', 'im'), 
		           ('ons', 'aist', 'est'), 
		           ('om', 'aem', 'em'), 
		           ('os', 'ais', 'es'), 
		           ('o', 'ai', 'ei'),
		           ('a', 'i', 'e')
		)
		pessoa = (6, 5, 4, 2, 1, 3)
		temp_verb = ('presente', 'futuro', 'pretérito')
		b = False
		for i in p7:
			for a in i:
				if a == palavra[-(len(a)):]: 
					b = True
					break
			if b == True:
					break
		if b == True:
			palavra2 = palavra[:-(len(a))]
			tv = temp_verb[i.index(a)]	
			pessoa2 = pessoa[p7.index(i)]	
			print(f'{palavra} - verbo {palavra2}en, {tv}, {pessoa2}a pessoa')
		else:
			print(f'{palavra} - não é um tempo verbal')
	
if __name__ == '__main__':
	main()
