from abc import abstractmethod 

class Problema:


    """
    A classe Problema atua como o esqueleto central do modelo, define as regras globais 
    do "jogo" que o algoritmo vai tentar resolver. 
    Quando esta classe é inicializada através do método __init__,  recebe e guarda 
    o ponto de partida do problema, o estado_inicial e a lista de todas as ações que são 
    permitidas realizar os operadores. 

    O método objectivo é uma função de teste crucial, recebe um estado qualquer e 
    verifica se o estado em que se encontra corresponde ao estado final queremos atingir, 
    funciona como o critério de paragem para o algoritmo. Sendo um método abstrato 
    a sua lógica será implementada nas subclasses.
    """


    def __init__(self, estado_inicial, operadores):
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    @abstractmethod
    def objectivo(self, estado):
        pass

    @property
    def estado_inicial(self):
        return self.__estado_inicial
    
    @property
    def operadores(self):
        return self.__operadores
