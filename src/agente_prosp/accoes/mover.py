from ecr.accao import Accao
from sae import Movimento

class Mover(Movimento, Accao):

    # representa um movimento na direcao indicada e passo de uma unidade

    def __init__(self, direcao):
        super().__init__(direcao, 1) # chama o construtor da classe Movimento