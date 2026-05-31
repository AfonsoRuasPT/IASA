from abc import abstractmethod 

'''
O Problema é o elemento central do Modelo do Problema (slide 13 Parte3):
define as regras globais que o algoritmo vai tentar resolver.
É composto por três elementos fundamentais:
  Estado inicial – ponto de partida da procura
  Operadores     – conjunto de acções possíveis
  Função objectivo – critério de paragem (estado → True/False)
'''

class Problema: # classe base do modelo do problema; define o contrato que qualquer problema de procura deve cumprir

    '''
    Problema define o modelo formal de um problema.
    Guarda o estado inicial e os operadores disponíveis, e declara o método abstracto objectivo() que cada problema concreto implementa com o seu
    critério de paragem específico.

    Problema é composto por Estado (estado_inicial) e por Operador (lista de operadores).
    '''

    """
    A classe Problema atua como o esqueleto central do modelo, define as regras globais do "jogo" que o algoritmo vai tentar resolver. 
    Quando esta classe é inicializada através do método __init__,  recebe e guarda o ponto de partida do problema, o estado_inicial e a lista de todas as ações que são 
    permitidas realizar os operadores. 

    O método objectivo é uma função de teste crucial, recebe um estado qualquer e 
    verifica se o estado em que se encontra corresponde ao estado final queremos atingir, 
    funciona como o critério de paragem para o algoritmo. Sendo um método abstrato 
    a sua lógica será implementada nas subclasses.
    """

    def __init__(self, estado_inicial, operadores): # recebe o estado inicial e a lista de operadores que definem o problema
        self.__estado_inicial = estado_inicial # atributo privado: Estado de partida da procura
        self.__operadores = operadores # atributo privado: lista de Operador disponíveis para gerar estados sucessores

    @abstractmethod
    def objectivo(self, estado): # método abstracto: cada subclasse define como verificar se um estado é o objectivo
        pass

    @property
    def estado_inicial(self): # propriedade de leitura: devolve o estado inicial; usado por MecanismoProcura para criar o nó raiz
        return self.__estado_inicial
    
    @property
    def operadores(self): # propriedade de leitura: devolve a lista de operadores; usado por _expandir() para gerar sucessores
        return self.__operadores