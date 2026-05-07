from lib.ecr.reaccao import Reaccao
from .resposta_mover import RespostaMover
from .estimulo_alvo import EstimuloAlvo

class AproximarDir(Reaccao):
    """
    AproximarDir é uma reaccao que tem como objetivo aproximar o agente ao alvo.
    Sendo uma reaccao passa nos seu construtor um estimulo e uma resposta.
    Tem como estimulo o EstimuloAlvo, que deteta a intencidade do alvo, e como resposta o RespostaMover, que tem a accao de mover 
    o agente na direccao do alvo.
    """

    def __init__(self, direccao):
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao)) # chama o construtor da classe Reaccao, passando uma instancia de RespostaMover com a direcao dada