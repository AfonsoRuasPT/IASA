from .procura_prof_lim import ProcuraProfLim
 
'''
A Procura em Profundidade Iterativa Iterative Deepening Search combina as vantagens da procura em profundidade (memória linear O(bd)) com
as da procura em largura (completa e óptima). 
Realiza sucessivas procuras em profundidade limitada com limites crescentes até encontrar a solução.
'''
 
class ProcuraProIter(ProcuraProfLim): # herda de ProcuraProfLim; executa procuras sucessivas com limites crescentes
 
    '''
    ProcuraProIter executa ProcuraProfLim repetidamente com profundidade máxima crescente até encontrar solução. 
    Combina memória linear com completude e optimalidade.
 
    ProcuraProIter herda de ProcuraProfLim.
    '''
 
    """
    A classe ProcuraProIter executa várias procuras em profundidade limitada sucessivas, aumentando o limite passo a passo 
    (inc_prof) dentro de um ciclo for até bater num limite absoluto (limite_prof). 
    Este mecanismo de procura consegue encontrar a melhor solução, mas gastando apenas a memória linear estrita da procura em 
    profundidade.
    """
 
    def procurar(self, problema, inc_prof=1, limite_prof=100): # executa ProcuraProfLim com limites crescentes
        for prof_max in range(0, limite_prof + 1, inc_prof): # range(0, limite+1, inc)
            solucao = super().procurar(problema, prof_max) # executa procura em profundidade limitada com o limite actual
            if solucao: # se encontrou solução, termina e devolve a solucao
                return solucao
        # se chegou ao limite absoluto sem solução, devolve None