from abc import ABC, abstractmethod

'''
ModeloPlan é a interface que define o contrato do modelo de planeamento que é como o conjunto mínimo de informação que qualquer planeador necessita para funcionar.
Um planeador precisa de saber:
  - Qual o estado actual do agente (obter_estado)
  - Quais os estados válidos do ambiente (obter_estados)
  - Quais os operadores aplicáveis (obter_operadores)
O ModeloMundo implementa esta interface, permitindo ser usado directamente pelo planeador.
'''

class ModeloPlan(ABC): # interface que define o contrato do modelo de planeamento

    '''
    ModeloPlan define o contrato mínimo que qualquer modelo de planeamento deve cumprir.
    Qualquer classe que realize esta interface pode ser usada pelo PlaneadorPEE para construir e resolver o problema de planeamento.

    ModeloPlan é realizado por ModeloMundo.
    É usado por ProblemaPlan.
    '''

    @abstractmethod
    def obter_estado(self): # devolve o estado actual do agente (EstadoAgente)
        """"""

    @abstractmethod
    def obter_estados(self): # devolve a lista de todos os estados do ambiente
        """"""

    @abstractmethod
    def obter_operadores(self): # devolve a lista de operadores
        """"""