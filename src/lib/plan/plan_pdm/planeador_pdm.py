from plan.planeador import Planeador
from plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from pdm.pdm import PDM
from .plano_pdm import PlanoPDM

class PlaneadorPDM(Planeador):

    '''
    O PlaneadorPDm cria uma instancia de modelo pdm plano que tem a informacao necessaria para a resolocao do markov
    
    '''

    def __init__(self, gama = 0.9, delta_max = 1):
        self.__gama = gama
        self.__delta_max = delta_max

    def planear(self, modelo_plan, objectivos):
        modelo_pdm = ModeloPDMPlan(modelo_plan, objectivos) # cria o modelo pdm plano
        pdm = PDM(modelo_pdm, self.__gama, self.__delta_max) 
        utilidade, politica = pdm.resolver() # fazer resolver a utilidade e politica
        return PlanoPDM(utilidade, politica) # criar a instancia PlanoPDM e retorna a