from .avaliador import Avaliador

class AvaliadorHeur(Avaliador):

    """
    A classe AvaliadorHeur funciona como um molde de base para qualquer avaliador que precise de usar adivinhações/estimativas,
    heurísticas, para tomar decisões, como é o caso da Procura Sófrega e da Procura A*. 
    Em vez de implementar logo uma regra, esta classe cria um espaço de memória seguro (self.__heuristica) para guardar o objeto 
    da heurística. 
    Ao usar o @property (getter) e o @heuristica.setter, ela permite-nos tanto ler como alterar a função de estimativa de forma 
    controlada a partir de outras partes do código.
    """

    def __init__(self):
        self.__heuristica = None
    
    @property
    def heuristica(self):
        return self.__heuristica
    
    @heuristica.setter
    def heuristica(self, heuristica):
        self.__heuristica = heuristica