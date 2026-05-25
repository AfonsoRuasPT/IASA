from ecr.accao import Accao
from sae import Movimento

class Mover(Movimento, Accao): # herança múltipla
 
    '''
    Mover representa o movimento do agente numa direcção específica com passo de 1 unidade.
    É usado pela RespostaMover para aproximar o agente de um alvo detectado.
 
    Mover herda de Movimento e Accao).
    '''
 
    # representa um movimento na direcao indicada e passo de uma unidade
 
    def __init__(self, direcao):
        super().__init__(direcao, 1) # chama o construtor da classe Movimento com a direcção indicada e passo de 1