from plan.plano import Plano

'''
Cada passo do plano contém:
  passo.estado    - o EstadoAgente em que o operador deve ser aplicado
  passo.operador  - o OperadorMover a aplicar nesse estado
A verificação passo.estado == estado em obter_accao() é fundamental pois garante que o plano está sincronizado com a posição real do agente.
Se o agente for desviado por algum motivo, a dessincronização é detectada e o ControloDelib invalida o plano e força replaneamento.
'''

'''
O Plano é o resultado do processo de planeamento: uma sequência ordenada de passos (estado + operador) que o agente deve executar para atingir o objectivo.
O PlanoPEE encapsula a solução e disponibiliza-a passo a passo ao ControloDelib através de obter_accao().
'''

class PlanoPEE(Plano):

    '''
    PlanoPEE herda de Plano.
    PlanoPEE tem uma associação com Solucao..
    '''

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