from mod.operador import Operador
from agente_prosp.accoes.mover import Mover
from .estado_agente import EstadoAgente
import math

'''
Na PEE um Operador define uma transformação, dado um estado, produz um estado sucessor.
O OperadorMover simula o movimento do agente numa determinada direcção, calculando a nova posição por translação geométrica:
  dx = passo * cos(ang)
  dy = -passo * sin(ang)
Esta simulação é feita pelo planeador durante a procura, sem que o agente se "mova mesmo".
'''

class OperadorMover(Operador):

    '''
    OperadorMover representa uma acção de movimento do agente numa direcção específica.
    É usado pelo planeador durante a simulação interna para explorar o espaço de estados, dado um EstadoAgente calcula o EstadoAgente sucessor aplicando a translação geométrica
    correspondente à direcção e verifica se o estado resultante é válido no ModeloMundo.
    O custo do operador é a distância euclidiana entre os dois estados.
 
    OperadorMover herda de Operador.
    OperadorMover tem uma associação com ModeloMundo.
    OperadorMover tem uma associação com Mover.
    '''

    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__ang = direccao.value # como estamos a trabalhat numa grd os angilos vao ser 0, 90, 180, 270 e 360
        self.__accao = Mover(direccao) # instancia Mover com a direccao

    def __repr__(self): # retorna uma String, fucao so python Representation, é como um toString
        return "OperadorMover(%s)" % self.accao # verifica se um estado pertence aos estados do modelo
    
    def __contains__(self, estado): # metodo no python Contains, metodo envocado quando utilizamos o "in"
        return estado in self.__estados

    def aplicar(self, estado): # este metodo tem como objectivo aplicar o operador mover, ou seja calcula a posicao do estado sucessor e retorna o novo estado do agente
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
    # ou seja o custo é a distancia

    @property
    def ang(self):
        return self.__ang

    @property
    def accao(self):
        return self.__accao