from agente.percepcao import Percepcao

class PercepcaoJogo(Percepcao): # herda de Percepcao, concretiza o tipo percepção para o contexto do jogo

    '''
    PercepcaoJogo é a concretização de Percepcao no contexto do jogo.

    PercepcaoJogo tem uma associação com EventoJogo.
    '''

    def __init__(self, evento): # recebe o EventoJogo como parametro
        self.__evento = evento

    @property
    def evento(self): # propriedade de leitura (read only)
        return self.__evento # devolve o EventoJogo encapsulado