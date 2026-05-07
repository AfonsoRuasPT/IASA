from .procura_prof_lim import ProcuraProfLim

class ProcuraProIter(ProcuraProfLim):


    """
    A classe ProcuraProIter executa várias procuras em profundidade limitada sucessivas, aumentando o limite passo a passo 
    (inc_prof) dentro de um ciclo for até bater num limite absoluto (limite_prof). 
    Este mecanismo de procura consegue encontrar a melhor solução, mas gastando apenas a memória linear estrita da procura em 
    profundidade.
    """

    def procurar(self, problema, inc_prof=1, limite_prof=100):
        for prof_max in range(0, limite_prof + 1, inc_prof):
            solucao = super().procurar(problema, prof_max) 
            if solucao:
                return solucao