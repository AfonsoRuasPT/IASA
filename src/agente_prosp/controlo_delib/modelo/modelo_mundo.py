from .operador_mover import OperadorMover
from sae.ambiente.direccao import Direccao
import math
from .estado_agente import EstadoAgente
from sae.ambiente.elemento import Elemento
from plan.modelo.modelo_plan import ModeloPlan

'''
Na arquitectura deliberativa o Modelo do Mundo é a representa o ambiente que suporta os mecanismos de deliberação e planeamento.
É actualizado a cada percepção e "alimenta" o planeador com os estados válidos e os operadores que se podem aplicar, permitindo ao agente simular o futuro antes de agir.
O ModeloMundo implementa a interface ModeloPlan de modo a poder ser utilizado directamente no contexto de um planeador sem necessidade de conversão.
'''

class ModeloMundo(ModeloPlan):

    def __init__(self):

        '''
        ModeloMundo é a "memória" do agente deliberativo. Mantém infromações de estado actual do agente, todos os estados, os operadores de movimento e um dicionário que mapeia
        posições para elementos (ALVO, OBSTACULO, VAZIO).
        É actualizado a cada percepção e serve de base tanto à deliberação (MecDelib consulta obter_estados e obter_elemento) como ao planeamento (PlaneadorPEE usa obter_estado,
        obter_estados, obter_operadores via interface ModeloPlan).
 
        ModeloMundo realiza ModeloPlan herda/implementa a interface.
        ModeloMundo é composto por OperadorMover, cria a lista de operadores no construtor.
        ModeloMundo compõe ControloDelib, criado no contrutor.
        ModeloMundo é usado por MecDelib, associação.
        '''

        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao] # cria um OperadorMover para cada direcção possível
        self.__elementos = {}  # dicionário que mapeia Posicao  Elemento
        self.__estado = None # estado actual do agente, iniciado a None
        self.__estados = [] #  # lista de todos os EstadoAgente
        self.__alterado = False # indica se o modelo foi alterado na actualização

    def obter_estado(self): # implementação do contrato ModeloPlan
        return self.__estado # devolve o EstadoAgente actual do agente
 
    def obter_estados(self): # implementação do contrato ModeloPlan
        return self.__estados # devolve a lista de todos os EstadoAgente válidos do ambiente
 
    def obter_operadores(self): # implementação do contrato ModeloPlan
        return self.__operadores # devolve a lista de OperadorMover
 
    def obter_elemento(self, estado):
        """
        Acede ao dicionário elementos e retorna o Elemento presente no EstadoAgente fornecido, obstáculos ou espaço vazio.
        """
        return self.__elementos.get(estado.posicao) # usa .get() para devolver None se a posição não existir no dicionário, evitando KeyError
 
    def distancia(self, estado): # calcula a distância euclidiana entre um estado e o estado actual do agente
        return math.dist(estado.posicao, self.__estado.posicao)
        # calcula a distancia euclidiana do estado que é passado ao estado atuals
 
    def actualizar(self, percepcao): # actualiza o modelo do mundo com base na percepção recebida
        self.__estado = EstadoAgente(percepcao.posicao) # cria um novo EstadoAgente com a posição actual do agente
        self.__alterado = self.__elementos != percepcao.elementos # verifica se os elementos do ambiente mudaram em relação à percepção anterior
        # se os elementos que constituem atualmente o modelo do mundo forem diferentes daqueles da percepcao, entao o modelo do mundo mudou
        if self.__alterado: # so actualiza estados e elementos se houve mudança, optimizando o desempenho
            self.__elementos = percepcao.elementos # actualiza o dicionário Posicao Elemento com os dados da percepção
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes] # cria a lista de EstadoAgente
 
    def mostrar(self, vista): 
        for posicao, elemento in self.__elementos.items(): 
            # metodo items() dá uma lista de (chave, valor) as chaves são as posições e os valores são os elementos
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]: # só mostra alvos e obstáculos
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao) # marca a posição actual do agente na vista
 
    def __contains__(self, estado): # método especial do python
        return estado in self.__estados # verifica se um EstadoAgente pertence à lista de estados válidos do modelo
 
    @property
    def alterado(self): # propriedade de leitura (read only)
        return self.__alterado # devolve True se o modelo foi alterado na última percepção; usado por ControloDelib.__reconsiderar
 
    @property
    def elementos(self): # propriedade de leitura (read only)
        return self.__elementos # devolve o dicionário Posicao Elemento