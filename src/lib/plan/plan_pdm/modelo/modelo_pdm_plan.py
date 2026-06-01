from plan.modelo.modelo_plan import ModeloPlan
from pdm.modelo.modelo_pdm import ModeloPDM

"""
O ModeloPDMPlan une os contratos ModeloPlan e ModeloPDM numa única classe, permitindo que o mesmo objecto
seja usado em varias classes com varios fins.
"""

"""
O ModeloPDMPlan é um "adaptador" que serve para traduzir entre dois contratos diferentes. 
O PlaneadorPDM tem acesso ao ModeloMundo através da interface ModeloPlan (obter_estado, obter_estados, obter_operadores), mas o PDM e o
MecUtil "não falam essa lingua" e precisam do tuplo formal do PDM (S, A, T, R) definido pela interface ModeloPDM. 
O ModeloPDMPlan resolve isso ao receber o ModeloMundo, transformar a sua informação na linguagem do PDM e servir ambos os contratos
simultaneamente através de herança múltipla.
"""

class ModeloPDMPlan(ModeloPlan, ModeloPDM): # herda tanto de ModeloPlan como de ModeloPDM

    """
    ModeloPDMPlan realiza simultaneamente ModeloPlan e ModeloPDM.
    """


    def __init__(self, modelo_plan, objectivos, rmax = 1000):
        self.__modelo_plan = modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax

        # Gerar transições de estado possíveis
        # Pré-cálculo de todas as transições possíveis (estado, operador) -> sucessor.
        # Feito aqui no construtor para optimizar as chamadas
        self.__transicoes = {} # dicionario que mantem todas as transicoes possiveis para este problema
        for s in self.obter_estados():
            for a in self.obter_operadores():
                sn =a.aplicar(s)
                self.__transicoes[(s, a)] = sn

    # Delegação

    def obter_estado(self):
        return self.__modelo_plan.obter_estado() # estado actual do agente

    def obter_estados(self):
        return self.__modelo_plan.obter_estados() # todos os estados válidos

    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores() # lista de OperadorMover

    def S(self):
        return self.obter_estados() # retorna a lista de Estados
    
    def A(self, s):
        return self.obter_operadores() if s not in self.__objectivos else [] # retorna uma lista de Operadores se s nao for um estado objectivo

    def T(self, s, a, sn):
        # verificamos o sn com o sn das transicoes, se for o mesmo retornamos, se forem diferentes é porque a transicao é diferente
        '''
        sn_temp = self.__transicoes.get((s, a))
        if sn == sn_temp:
            return 1.0 if sn not None else 0.0
        else:
            return 0.0
        '''
        sn = self.__transicoes.get((s, a))
        return 1.0 if sn is not None else 0.0
        # retorna a probabilidade de transição 1.0 se a transição de s para sn através de a é válida, retorna 0.0 caso contrário.

    def R(self, s, a, sn):
        r = -a.custo(s, sn)
        if sn in self.__objectivos:
            r += self.__rmax
        return r
        # retorna a recompensa da transição, penaliza o custo do movimento e recompensa o agente se sn for um estado objectivo.


    def suc(self, s, a):
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else []
        # retorna a lista com o estado sucessor de s ao aplicar a acção a, ou lista vazia se o movimento nao for valido.
