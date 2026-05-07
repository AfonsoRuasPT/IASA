from .procura_melhor_prim import ProcuraMelhorPrim
from .aval.avaliador_custo_unif import AvaliadorCustoUnif

class ProcuraCustoUnif(ProcuraMelhorPrim):

    """
    A classe ProcuraCustoUnif concretiza o algoritmo de Procura de Custo Uniforme, que é um caso particular da Procura Melhor-Primeiro. 
    O código apenas invoca o construtor da superclasse injetando-lhe o AvaliadorCustoUnif. 
    Isto significa que a fronteira vai passar a ser ordenada estritamente pelo custo real e acumulado desde a partida até ao nó 
    em questão. 
    O objetivo é ignorar a quantidade de passos (profundidade) e garantir a melhor solução com base no caminho mais barato 
    (menor distância, menor tempo, etc.).
    """
    
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())