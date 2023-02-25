"""
-- DOC --
mostrar():
- define o valor de a e b do vetor
>>> vet1.mostrar()
A = 1
B = 2
    
cord():
- retorna uma string de representação na forma "<a,b>".
>>> vet1.cord()
<1,2>

modulo():
- calcula e retorna o modulo do vetor.
>>> vet1.modulo()
2.5

__add__(), __sub__(), __mul__(): 
-operações basicas por meio da sobrecarga de operadores.
>>> vet1 + vet2
<4,6>
>>> vet1 - vet2
<-2,-2>
>>> vet1 * vet2
6
"""

class vetor:
	def __init__(self, a, b):
		self.__a = a
		self.__b = b
		
	def __add__(self, other):
		a1=  self.__a + other.__a
		b1 = self.__b + other.__b
		return f'<{a1},{b1}>'
		
	def __sub__(self, other):
		a1=  self.__a - other.__a
		b1 = self.__b - other.__b
		return f'<{a1},{b1}>'
	
	def __mul__(self, other):
		a1=  self.__a * other.__a
		b1 = self.__b * other.__b
		a3 = a1 + a1
		return a3
	
	def mostrar(self):
		return f'a = {self.__a}\nb = {self.__b}'
		
	def cord(self):
		return f'<{self.__a},{self.__b}>'
		
	def modulo(self):
		return ((self.__a)**2 + (self.__b)*2)*0.5
