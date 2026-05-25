from .comportamento_comp import ComportamentoComp

'''
A selecção por Hierarquia é um mecanismo de selecção de acção onde os comportamentos estão organizados numa hierarquia fixa de subsunção.
A ordem dos comportamentos na lista define a prioridade, o primeiro comportamento activado tem sempre precedência sobre os restantes.
Camadas superiores têm prioridade sobre camadas inferiores.
No Agente Prospector, a hierarquia é: AproximarAlvo > EvitarObst > Explorar.
'''

class Hierarquia(ComportamentoComp): # herda de ComportamentoComp

    '''
    Hierarquia implementa o mecanismo de selecção de acção por hierarquia fixa. 
    Selecciona sempre a primeira acção da lista, ou seja, a acção gerada pelo sub-comportamento de maior nível de competência que foi activado perante a percepção actual.

    Hierarquia herda de ComportamentoComp.
    '''
    
    def seleccionar_accao(self, accoes): # implementação do método abstracto de ComportamentoComp
        """Ordem de prioridade - Prioridade é a ordem dos elementos da lista de forma fixa"""
        if accoes: # pode nao ser redundante se chamarmos a hierarquia sem ser pelo metodo activar da class ComportamentoComposto
            return accoes[0] # devolve sempre o primeiro elemento