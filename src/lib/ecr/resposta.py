class Resposta:

    # Define uma resposta a estímulos, em termos de acção a realizar e da respectiva prioridade

    def __init__(self, accao):
        self._accao = accao # protected

    def activar(self, percepcao, intencidade = 0): # retorna accao
        accao_atual = self._obter_accao(percepcao)
        
        # 2. Verificamos se a ação realmente existe (se não é None)
        if accao_atual is not None: 
            accao_atual.prioridade = intencidade
        return accao_atual


        


    def _obter_accao(self, percepcao): # retorna a accao
        return self._accao