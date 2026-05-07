from mod.operador import Operador
from agente_prosp.accoes.mover import Mover
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

    def aplicar(self, estado):
        pass

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