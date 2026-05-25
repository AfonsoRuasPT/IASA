from .comportamento import Comportamento

'''
A Reacção é o elemento base da arquitectura reactiva.
Representa uma regra estímulo-resposta, dado um estímulo detectado na percepção, gera uma resposta que produz uma acção.
O modelo de interacção da Reacção:
  1 - activar(percepcao) é chamado
  2 - O Estímulo detecta a intensidade do estímulo na percepção
  3 - Se intensidade > 0, a Resposta é activada com a percepção e a intensidade
  4 - A Resposta define a prioridade da acção igual à intensidade e devolve a acção
'''

class Reaccao(Comportamento): # herda de Comportamento, implementa o mecanismo base de uma reacção simples

    '''
    Reaccao implementa o mecanismo base de uma reacção.
    Associa um Estímulo a uma Resposta.
    Se o estímulo não for detectado (intensidade = 0), a reacção não é activada e nãodevolve acção.

    Reaccao herda de Comportamento.
    Reaccao compõe Estimulo.
    Reaccao compõe Resposta.
    '''

    """
    Módulo ECR (Esquemas Comportamentais Reactivos) representa uma forma modular sobre o funcionamento agentes reativos e os seus comportamentos.
    """

    def __init__(self, estimulo, resposta): # recebe o estímulo e a resposta que definem esta reacção
        # A reaccao é um modulo que associa estimulos e respostas
        self.__estimulo = estimulo # Estimulo concreto que detecta a presença do estímulo
        self.__resposta = resposta # Resposta concreta que gera a acção

    def activar(self, percepcao): # implementação do contrato de Comportamento, implementado com o apoio do diagrama de sequencia on pdf da arquitetura slide 4
        intencidade = self.__estimulo.detectar(percepcao) # o estimulo deteta a intensidade do estimulo a partir da percepcao
        if intencidade > 0: # só activa a resposta se o estímulo for detectado
            accao = self.__resposta.activar(percepcao, intencidade) # a resposta activa a acção
            return accao # retorna a accao