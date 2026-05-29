from plan.modelo.modelo_plan import ModeloPlan
from pdm.modelo.modelo_pdm import ModeloPDM

class ModeloPDMPlan(ModeloPlan, ModeloPDM):

    def __init__(self, modelo_plan, objectivos, rmax = 1000):
        self.__modelo_plan = modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax

        # Gerar transições de estado possíveis

        self.__transicoes = {} # dicionario que mantem todas as transicoes possiveis para este problema
        for s in self.obter_estados():
            for a in self.obter_operadores():
                sn =a.aplicar(s)
                self.__transicoes[(s, a)] = sn

    # Delegação

    def obter_estado(self):
        return self.__modelo_plan.obter_estado()

    def obter_estados(self):
        return self.__modelo_plan.obter_estados()

    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()

    def S(self):
        return self.obter_estados()
    
    def A(self, s):
        return self.obter_operadores() if s not in self.__objectivos else []

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

    def R(self, s, a, sn):
        r = -a.custo(s, sn)
        if sn in self.__objectivos:
            r += self.__rmax
        return r

    def suc(self, s, a):
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else []
