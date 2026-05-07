from .comportamento_comp import ComportamentoComp

class Prioridade(ComportamentoComp):
    
    def seleccionar_accao(self, accoes):
        """A acção tem uma prioridade assiciada, na lista de acções temos uma prooridade associada e temos de retornar a acção com maior prioridade"""
        
        """ -- MINHA IMPLEMENTAÇÃO DO METODO --
        if accoes:
            max_prioridade = 0 # inicializamos a prioridade a 0
            for accao in accoes: # corremos todas as accoes na lista
                prioridade = accao.prioridade # vemos qual a prioridade dessa mesma accao
                if prioridade >= max_prioridade: # se a prioridade for maior que a prioridade maxima até agora atualizamos a vareavel max_prioridade e a accao que vamos retornar
                    max_prioridade = prioridade # atualizamos a vareavel max_prioridade
                    accao_a_retornar = accao # atualizamos a variavel accao_a_retornar
            return accao_a_retornar # retornamos a accao com maior prioridade
        """
        # IMPLEMENTAÇÃO DADA PELO PROFESSOR
        """
        A função max percorre a lista de accoes de forma automática a procura da "max/maior". 
        A parte key=lambda serve apenas para avisar o Python de que deve usar o valor da prioridade
        para fazer essa comparação entre elas. 
        A função devolve a ação que tiver o número de prioridade maior.
        """
        return max(accoes, key=lambda accao: accao.prioridade)

    