from plan.planeador import Planeador
from pee.melhor_prim.procura_aa import ProcuraAA
from .plano_pee import PlanoPEE
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan

# src\lib\plan\plan_pee\mod_prob\heur_dist.py # relative path
# src\lib\plan\plan_pee\mod_prob\problema_plan.py # relative path

# src\lib\plan\plan_pee\planeador_pee.py # caminho relatico desta class
class PlaneadorPEE(Planeador):

    def __init__(self):
        self.__mec_pee = ProcuraAA()

    def planear(self, modelo_plan, objectivos):
        objectivo = objectivos[0]
        problema = ProblemaPlan(modelo_plan, objectivo)
        heuristica = HeurDist(objectivo)
        solucao = self.__mec_pee.procurar(problema, heuristica)
        return PlanoPEE(solucao)