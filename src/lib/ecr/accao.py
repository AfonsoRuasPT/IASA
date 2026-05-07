from agente.accao import Accao as AccaoAgente # na pag 3 do projeto é indicado numa restricao que a class accao deve herdar da classe Accao
                                              # como os nomes sao iguais fazemos o "as" para evitar conflitos de nomes, e assim podemos usar o nome Accao para a nossa classe sem problemas

class Accao(AccaoAgente):

    def __init__(self, prioridade = 0):
        self.__prioridade = prioridade

    @property # getter
    def prioridade(self):
        return self.__prioridade
    
    @prioridade.setter # setter
    def prioridade(self, valor):
        self.__prioridade = valor
        
        