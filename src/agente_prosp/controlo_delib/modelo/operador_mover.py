from mod.operador import Operador
from agente_prosp.accoes.mover import Mover
from .estado_agente import EstadoAgente
import math

class OperadorMover(Operador):

    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__ang = direccao.value
        self.__accao = Mover(direccao)

    def __repr__(self): # retorna uma Strinf, fucao so python Representation, é como um toString
        return "OperadorMover(%s)" % self.accao
    
    def __contains__(self, estado): # metodo no python Contains, metodo envocado quando utilizamos o "in"
        return estado in self.__estados

    def aplicar(self, estado): # este metodo tem como objectivo aplicar o operador mover, ou seja calcura a posicao do estado sucessor e retorna o novo estado do agente
        x = estado.posicao[0] # obter a coordenada x da posicao do estado
        y = estado.posicao[1] # obter a coordenada y da posicao do estado
        dy = -self.__accao.passo * math.sin(self.__ang) # calcular dy conforme a formula no slide 5 da parte 4 do projeto
        dx = self.__accao.passo * math.cos(self.__ang) # calcular dx conforme a formula no slide 5 da parte 4 do projeto
        nova_posicao = (x + dx, y + dy) # crontruir o tuplo da nova posicao que é adicionar o dx e dy a posicao atual
        estado_suc = EstadoAgente(nova_posicao) # criar estado sucessor com a nova possicao
        if estado_suc in self.__modelo_mundo: # verificamos se o estado pertente ao modelo do mundo
            return estado_suc # retornar o novo estado agente  
    
    def custo(self, estado, estado_suc):
        return max(math.dist(estado.posicao, estado_suc.posicao), 1) 
    # calcular distancia euclidiana e retornar o custo, se o custo calculado for maior que 1 retornamos o custo calculado,
    # se nao retornamo 1

    @property
    def ang(self):
        return self.__ang

    @property
    def accao(self):
        return self.__accao