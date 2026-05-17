from plan.plano import Plano

class PlanoPEE(Plano):

    def __init__(self, solucao):
        self.__solucao = solucao
        self.__passos = [passo for passo in solucao] # os passos sao uma lista de instancia de espaco para cada passo da solucao

    def obter_accao(self, estado):
        if self.__passos: # verificamos se existem passos
            passo = self.__passos.pop(0) # retiramos o primeiro passo da lista
            if passo.estado == estado: # se estado for o mesmo entao o plano esta sincronizado com o agente
                return passo.operador # retornamos o operador so passo

    def mostrar(self,vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao,passo.operador.ang)