from agente.accao import Accao as AccaoAgente # na pag 3 do projeto é indicado numa restricao que a class accao deve herdar da classe Accao
                                              # como os nomes sao iguais fazemos o "as" para evitar conflitos de nomes, e assim podemos usar o nome Accao para a nossa classe sem problemas

'''
Accao estende o conceito de acção da Parte 1 acrescentando o atributo prioridade. 
A prioridade é definida pela Resposta igual à intensidade do estímulo detectado.
'''

class Accao(AccaoAgente): # herda de AccaoAgente

    '''
    Accao herda de AccaoAgente.
    '''

    def __init__(self, prioridade = 0): # prioridade inicializada a 0
        self.__prioridade = prioridade 

    @property # getter
    def prioridade(self): # propriedade de leitura pública
        return self.__prioridade # devolve a prioridade actual da acção
    
    @prioridade.setter # setter
    def prioridade(self, valor): # permite definir a prioridade externamente
        self.__prioridade = valor # actualiza a prioridade