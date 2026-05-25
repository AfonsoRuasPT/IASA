from abc import ABC, abstractmethod
 
'''
O Plano é a interface que define o contrato do resultado do planeamento.
Um plano mantem a sequência de passos gerada pelo planeador e permite obter incrementos da acção a executar em cada estado do agente.
'''
 
class Plano(ABC): # interface que define o contrato do plano de acção
 
    '''
    Plano define o contrato do resultado do processo de planeamento.
    Qualquer plano concreto deve implementar obter_accao e mostrar.
 
    Plano é realizado por PlanoPEE..
    '''
 
    @abstractmethod
    def obter_accao(self, estado): # dado o estado actual do agente, devolve o operador a executar
        """"""
 
    @abstractmethod
    def mostrar(self, vista): # renderiza o plano na vista gráfica
        """"""