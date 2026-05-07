from ecr.resposta import Resposta
from agente_prosp.accoes.mover import Mover

class RespostaMover(Resposta):
    """
    Resposta mover para o comportamento aproximar
    """

    def __init__ (self, direccao = None):
        super().__init__(Mover(direccao)) # chama o construtor da classe Resposta