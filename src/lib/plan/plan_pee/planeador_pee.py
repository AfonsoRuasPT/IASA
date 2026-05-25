from plan.planeador import Planeador
from pee.melhor_prim.procura_aa import ProcuraAA
from .plano_pee import PlanoPEE
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan

'''
O planeamento gera o plano para concretizar objectivos pré-definidos.
O PlaneadorPEE implementa este processo usando Procura A* (ProcuraAA).
Dado um ModeloPlan e uma lista de objectivos, constrói um ProblemaPlan, define a heurística HeurDist e invoca o mecanismo de procura para encontrar o percurso óptimo no espaço 
de estados.
'''

class PlaneadorPEE(Planeador):

    '''

    PlaneadorPEE herda de Planeador.
    PlaneadorPEE tem uma dependência com ProblemaPlan e HeurDist.
    PlaneadorPEE tem uma dependência com PlanoPEE.
    '''

    def __init__(self): # inicializa o mecanismo de procura A*
        self.__mec_pee = ProcuraAA() # instância da Procura A*
 
    def planear(self, modelo_plan, objectivos): # gera um plano para atingir o primeiro objectivo da lista
        objectivo = objectivos[0] # selecciona o primeiro objectivo da lista
        problema = ProblemaPlan(modelo_plan, objectivo) # constrói o problema de planeamento
        heuristica = HeurDist(objectivo) # instancia a heurística de distância euclidiana
        solucao = self.__mec_pee.procurar(problema, heuristica) # executa o A* e obtém a solução
        return PlanoPEE(solucao) # encapsula a solução num PlanoPEE