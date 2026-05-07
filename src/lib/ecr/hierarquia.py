from .comportamento_comp import ComportamentoComp

class Hierarquia(ComportamentoComp):
    
    def seleccionar_accao(self, accoes): # retorna uma accao
        """Ordem de prioridade - Prioridade é a ordem dos elementos da lista de forma fixa"""
        if accoes: # pode nao ser redundante se chamarmos a hierarquia sem ser pelo metodo activar da class ComportamentoComposto
            return accoes[0] # retornamos o indice 0 da lista accoes