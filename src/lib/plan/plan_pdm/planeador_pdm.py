from plan.planeador import Planeador
from plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from pdm.pdm import PDM
from .plano_pdm import PlanoPDM


"""
Planeamento com base em processos de decisao de markov PDM
Enquanto a PEE assume um ambiente determinista (cada acção tem um resultado certo), o PDM lida com ambientes não-deterministas, onde o resultado de uma acção pode ser incerto.

Num PDM, o planeamento não produz uma sequência fixa de acções (plano), mas sim uma politica, uma função que, para cada estado, indica a acção óptima a realizar.

A política óptima é calculada iterativamente usando a equação de Bellman que é a utilidade de cada estado é actualizada em função
das utilidades dos estados sucessores, até convergir.


Os estados futuros dependem apenas do estado presente, são independentes do histórico. 
Isto é o que torna o cálculo iterativo viável por programação dinâmica.
"""




class PlaneadorPDM(Planeador):

    '''
    Herda de Planeador.
    '''

    def __init__(self, gama = 0.9, delta_max = 1):
        self.__gama = gama # factor de desconto 
        # reflecte o efeito da passagem do tempo: recompensas
        # futuras valem menos do que imediatas. Y = 0.9 significa que uma
        # recompensa daqui a n passos vale 0.9^n do seu valor original.
        self.__delta_max = delta_max


    def planear(self, modelo_plan, objectivos): # cria o plano pdm
        modelo_pdm = ModeloPDMPlan(modelo_plan, objectivos) # cria o modelo pdm plano
        pdm = PDM(modelo_pdm, self.__gama, self.__delta_max) # criam uma instancia de pdm para poder calcular a utilidade e politica
        utilidade, politica = pdm.resolver() # calcula a utilidade e politica
        return PlanoPDM(utilidade, politica) # criar a instancia PlanoPDM e retorna a