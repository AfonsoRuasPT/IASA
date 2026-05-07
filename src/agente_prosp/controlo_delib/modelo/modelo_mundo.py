from operador_mover import OperadorMover
from sae.ambiente.direccao import Direccao
import math
from estado_agente import EstadoAgente
from sae.ambiente.elemento import Elemento

class ModeloMundo():

    """
    A classe ModeloMundo constitui a memória estruturada do agente no pacote modelo.
    Em estrita conformidade com o diagrama arquitetural fornecido, gere as instâncias de 
    EstadoAgente e mapeia-as para a enumeração Elemento do pacote sae através de um 
    dicionário. É a entidade que alimenta o planeador com os estados possíveis e os 
    operadores aplicáveis para simular o futuro[cite: 1].
    """

    def __init__(self):

        """
        Inicializa as estruturas base do modelo de representação. Cria os atributos privados 
        necessários para guardar o estado atual, a totalidade dos estados conhecidos, o 
        conjunto de operadores de movimento instanciados e o dicionário central de elementos 
        que define o conteúdo do ambiente[cite: 1].
        """

        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]
        self.__elementos = {}
        self.__estado = None
        self.__estados = []
        self.__alterado = False

    def obter_estado(self):
        return self.__estado

    def obter_estados(self):
        return self.__estados

    def obter_operadores(self):
        return self.__operadores

    def obter_elemento(self, estado):
        """
        Acede ao dicionário de leitura interno e retorna a instância da enumeração Elemento 
        presente no EstadoAgente fornecido, distinguindo entre alvos, obstáculos ou 
        espaço vazio.
        """
        # retornal elemento associado ao estado, mas pode nao haver, ent devemos usar o metodo get() porque assim se nao existir retorna None
        return self.__elementos.get(estado.posicao)

    def distancia(self, estado):
        return math.dist(estado.posicao, self.__estado.posicao)
        # calcula a distancia eucldiana do estado que é passado ao estado atual

    def actualizar(self, percepcao): # actualiza o modelo do mundo
        self.__estado = EstadoAgente(percepcao.posicao) # instancias o estado agente passando a percepcao.posicao
        self.__alterado = self.__elementos != percepcao.elementos # atualizar a vareavel, alterados
        # se os elementos que constituem atualmente o modelo do mundo forem diferntes daqueles da percepcao, entao o modelo do mundo mudou
        if self.__alterado:
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]

    def mostrar(self, vista):
        for posicao, elemento in self.__elementos.items(): 
            # metodo items() da uma lista dá (chave, valor) as chaves sao as posicoes e os valores sao os elementos

            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)

    @property
    def alterado(self):
        return self.__alterado

    @property
    def elementos(self):
        return self.__elementos 