from .comportamento import Comportamento

class Reaccao(Comportamento):

    """
    Módulo ECR (Esquemas Comportamentais Reactivos) representa uma forma modular sobre o funcionamento agentes reativos e os seus comportamentos.
    """


    def __init__(self, estimulo, resposta):
        
        # A reaccao é um modulo que associa estimulos e respostas
        self.__estimulo = estimulo
        self.__resposta = resposta

    def activar(self, percepcao): # diagrama de sequencia no Arquitectura de agentes reactivos - Parte 1.pdf slide 14
        intencidade = self.__estimulo.detectar(percepcao) # o estimulo deteta a intencidade do estimulo a partir da percepcao
        if intencidade > 0: # se a intencidade for maior que 0
            accao = self.__resposta.activar(percepcao, intencidade) # a resposta activa a accao
            return accao # retorna a accao
        