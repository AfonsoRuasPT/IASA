from ecr.comportamento import Comportamento
from agente_prosp.accoes.avancar import Avancar

class ExplorarMem(Comportamento):
    """
    Comportamento explorar com memoria, o agente tem uma memoria das posicoes e direcoes onde ja esteve, se o agente estiver numa posicao e 
    direcao onde ja esteve ele nao avança, caso contrario ele avança, a memoria tem um tamanho maximo definido por dim_max_mem, se a 
    memoria atingir esse tamanho o agente remove a posicao e direcao mais antiga da memoria para adicionar a nova posicao e direcao
    """

    def __init__(self, dim_max_mem = 100):
        self.__dim_max_mem = dim_max_mem
        self.__memoria = [] # memoria do agente iniciada vazia

    def activar(self, percepcao):
        dir_posicao = percepcao.posicao #obter a posicao atual do agente
        dir_direccao = percepcao.direccao #obter a direccao atual do agente
        posicao_direccao = (dir_posicao, dir_direccao) # contruir a tupla posicao_direcao com a posicao e direcao atual do agente
        if posicao_direccao in self.__memoria: # verificcar se a posicao e direccao atual do agente ja estao em memoria
            return # se estiverem nao retornamos nada
        elif len(self.__memoria) != self.__dim_max_mem: # verificamos se a memoria esta cheia
                self.__memoria.append(posicao_direccao) # como a memoria nao esta cheia, adicionamos o tuplo a memoria
                return Avancar() # retornamos a accao avancar
        else: # como a lista esta cheia
            self.__memoria.pop(0) # damos pop, ou seja, removemos o olemento mais antigo da memoria, o elemento com posicao 0, 
            self.__memoria.append(posicao_direccao) # adicionamos o tuplo a memoria
            return Avancar() # retornamos a accao Avancar