from mod.problema import Problema

class ProblemaPlan(Problema):

    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final

    def objectivo(self, estado):
        if estado == self.__estado_final:
            return True
        else:
            return False