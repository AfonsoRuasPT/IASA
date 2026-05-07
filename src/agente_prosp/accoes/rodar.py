from ecr.accao import Accao
from sae import Movimento

class Rodar(Movimento, Accao): 
    
    """ no python podemos ter heranca multipla, e quando chamamos a função super chamamos o contrutor
    da primeira classe, ou seja, da classe Movimento"""

    def __init__(self, direcao):
        super().__init__(direcao, 0) # chama o construtor da classe Movimento, com passo de 0 unidades (gira-se no mesmo sitio)
        