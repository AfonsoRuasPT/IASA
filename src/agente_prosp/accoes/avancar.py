from ecr.accao import Accao
from sae import Movimento
 
'''
As acções concretas (Mover, Avancar, Rodar) herdam de Accao (ECR) para ter o atributo prioridade e de Movimento (SAE) para serem executáveis no ambiente.
'''
 
class Avancar(Movimento, Accao): # herança múltipla: é uma Accao ECR (tem prioridade) e um Movimento SAE (pode ser actuado)
 
    '''
    Avancar representa o movimento do agente em frente na direcção actual, com passo de 1 unidade. 
 
    Avancar herda de Movimento e Accao.
    '''
    
    def __init__(self):
        super().__init__(None, 1) # chama o construtor da classe Movimento, com direcao None (direção que ja estava) e passo de 1 unidade