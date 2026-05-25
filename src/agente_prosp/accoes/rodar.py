from ecr.accao import Accao
from sae import Movimento

class Rodar(Movimento, Accao): # herança múltipla

    """ no python podemos ter heranca multipla, e quando chamamos a função super chamamos o contrutor
    da primeira classe, ou seja, da classe Movimento"""
 
    '''
    Rodar representa a rotação do agente para uma direcção específica sem avançar (passo 0).
    É usado por Explorar e por RespostaEvitar (rotação para evitar obstáculo).
 
    Rodar herda de Movimento e Accao.
    '''
 
    def __init__(self, direcao):
        super().__init__(direcao, 0) # chama o construtor da classe Movimento com a direcção indicada e passo 0 (gira no mesmo sítio)