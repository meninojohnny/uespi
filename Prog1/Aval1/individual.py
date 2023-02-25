class Individual:
    #pra controle de geração de sequenciamento de nomes automaticos
    __nomes = 0
    __genotipos = ['AA', 'Ai', 'BB', 'Bi', 'AB', 'ii']
    #pega as informações das instancias e armazena nesse dicionário
    __individuos = {}
    __sangue = {'AA':'A', 'Ai':'A', 'BB':'B', 'Bi':'B', 'AB':'AB', 'ii':'O'}
    __aglutinogeneos = {'AA':'A', 'Ai':'A', 'BB':'B', 'Bi':'B', 'AB':'A e B', 'ii':'Sem aglutinogeneos'}
    __aglutinina = {'AA':'Anti-B', 'Ai':'Anti-B', 'BB':'Anti-A', 'Bi':'Anti-A', 'AB':'Sem aglutinina', 'ii':'Anti-A e Anti-B '}
    def __init__(self, tipo, nome=None):
        self.__tipo = tipo
        if self.__tipo not in self.__genotipos:
            print('ERROR, ESSE GENOTIPO NÃO EXISTE')
            
        self.__nome = nome
        if self.__nome == None:
            a = Individual.__nomes + 1
            self.nome = 'Indiv' + str(a)
            Individual.__nomes = a
            if self.nome in Individual.__individuos:
                a = Individual.__nomes + 1
                self.__nome = 'Indiv' + str(a)
                Individual.__nomes = a
            Individual.__individuos[self.__nome] = self.__tipo
        elif self.__nome in Individual.__individuos:
            print(f'o nome {self.__nome} já existe, insira outro')
        else:
            Individual.__individuos[self.__nome] = self.__tipo
            
    #retorna o nome do idividuo        
    def name(self):
        return self.__nome
    
    #retorna o genotipo        
    def genotype(self):
        return Individual.__individuos[self.__nome]
    
    #retorna o tipo sanguineo   
    def blood_type(self):
        return Individual.__sangue[self.__tipo]

    #retorna os aglutinogeneos
    def agglutinogens(self):
        return Individual.__aglutinogeneos[self.__tipo]
        
    #retorna as aglutinias
    def agglutinins(self):
        return Individual.__aglutinina[self.__tipo]
    
    #faz o cruzamento e identifica se o individuo passado como parametro existe no sistema            
    def offsprings_blood_types(self, nome):
        if nome in Individual.__individuos:
            a = Individual.__individuos[self.__nome]
            b = Individual.__individuos[nome]
            if a == 'AA' and b == 'AA':
                return ('AA')
            elif a == 'AA' and b == 'Ai' or b == 'AA' and a == 'Ai' :
                return ('AA, Ai')
            elif a == 'AA' and b == 'BB' or b == 'AA' and a == 'BB' :
                return ('AB')
            elif a == 'AA' and b == 'Bi' or b == 'AA' and a == 'Bi' :
                return ('AB,Ai')
            elif a == 'AA' and b == 'AB' or b == 'AA' and a == 'AB' :
                return ('AA,AB')
            elif a == 'AA' and b == 'ii' or b == 'AA' and a == 'ii' :
                return ('Ai')
            elif a == 'Ai' and b == 'Ai':
                return ('AA, ii')
            elif a == 'Ai' and b == 'BB' or b == 'Ai' and a == 'BB' :
                return ('AB, Bi')
            elif a == 'Ai' and b == 'Bi' or b == 'Ai' and a == 'Bi' :
                return ('AB, ii')
            elif a == 'Ai' and b == 'AB' or b == 'Ai' and a == 'AB' :
                return ('AA, Bi')
            elif a == 'Ai' and b == 'ii' or b == 'Ai' and a == 'ii' :
                return ('Ai, ii')
            elif a == 'BB' and b == 'BB':
                return ('BB')
            elif a == 'BB' and b == 'AB' or b == 'BB' and a == 'AB' :
                return ('AB, BB')
            elif a == 'BB' and b == 'ii' or b == 'BB' and a == 'ii' :
                return ('Bi')
            elif a == 'Bi' and b == 'AB' or b == 'Bi' and a == 'AB' :
                return ('AB Bi')
            elif a == 'Bi' and b == 'ii' or b == 'Bi' and a == 'ii' :
                return ('Bi, ii')
            elif a == 'AB' and b == 'AB':
                return ('AA, BB')
            elif a == 'AB' and b == 'ii' or b == 'AB' and a == 'ii' :
                return ('Ai, Bi')
            elif a == 'ii' and b == 'ii':
                return ('ii')
        else:
            print(f'O NOME {nome} NÃO ESTÁ NO SISTEMA')
    
    #retorna se pode doar ou não e identifica se o individuo passado como parametro existe no sistema        
    def can_donate(self, nome):
        if nome in Individual.__individuos:
            a = Individual.__sangue[self.__tipo]
            b = Individual.__sangue[Individual.__individuos[nome]]
            if a == 'A' and (b == 'A' or b == 'AB'):
                return True
            elif a == 'B' and b == 'B' or b == 'AB':
                return True
            elif a == 'AB' and b == 'AB':
                return True
            elif a == 'O':
                return True
            else:
                return False
        else:
            print(f'O NOME {nome} NÃO ESTÁ NO SISTEMA')
    
    #retorna se pode recebr ou não e identifica se o individuo passado como parametro existe no sistema       
    def can_receive(self, nome):
        if nome in Individual.__individuos:
            b = Individual.__sangue[self.__tipo]
            a = Individual.__sangue[Individual.__individuos[nome]]
            if a == 'A' and (b == 'A' or b == 'AB'):
                return True
            elif a == 'B' and b == 'B' or b == 'AB':
                return True
            elif a == 'AB' and b == 'AB':
                return True
            elif a == 'O':
                return True
            else:
                False
        else:
            print(f'O NOME {nome} NÃO ESTÁ NO SITEMA')
            
"""
- Com esses códigos simples para teste, o programa atendeu os requisitos

from individual import Individual

p1 = Individual('AA', 'maria')
p2 = Individual('Bi', 'joao')
p3 = Individual('AB', 'pedro')
p4 = Individual('ii', 'marcos')

print(p1.name())
print(p2.genotype())
print(p3.blood_type())
print(p4.agglutinogens())
print(p1.agglutinins())
print(p2.can_donate('maria'))
print(p3.can_receive('joao'))
print(p4.offsprings_blood_types('pedro'))

- Mas na hora de adaptar ao código disponibilizado no git, não rodou... 

"""
