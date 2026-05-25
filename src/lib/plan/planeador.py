from abc import ABC, abstractmethod
 
'''
O Planeador é a interface que define o contrato do raciocínio da arquitectura deliberativa.
Define que qualquer planeador, independentemente do mecanismo de raciocínio, deve ser capaz de receber um modelo de planeamento e objectivos e devolver um Plano.
'''
 
class Planeador(): # interface que define o contrato do planeador
 
    '''
    Planeador define o contrato de raciocínio do agente deliberativo.
    Qualquer planeador concreto deve implementar o método planear, recebendo o modelo do problema e os objectivos e devolvendo um Plano.
    Esta interface permite que o ControloDelib use qualquer planeador sem conhecer
    a sua implementação concreta - baixo acoplamento.
 
    Planeador é realizado por PlaneadorPEE..
    '''
 
    @abstractmethod
    def planear(self, modelo_plan, objectivos): # dado um modelo de planeamento e objectivos, devolve um Plano
        """"""