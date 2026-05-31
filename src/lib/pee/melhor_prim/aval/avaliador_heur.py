from .avaliador import Avaliador
 
class AvaliadorHeur(Avaliador): # herda de Avaliador; base para avaliadores que usam heurística (Sôfrega e A*)
 
    '''
    AvaliadorHeur é a classe base para avaliadores que necessitam de uma função heurística h(n). 
    Guarda a heurística num atributo privado e expõe-a via getter/setter.
 
    AvaliadorHeur herda de Avaliador.
    '''
 
    """
    A classe AvaliadorHeur funciona como um molde de base para qualquer avaliador que precise de usar adivinhações/estimativas,
    heurísticas, para tomar decisões. 
    Em vez de implementar logo uma regra, esta classe cria um espaço de memória seguro (self.__heuristica) para guardar o objeto 
    da heurística. 
    Ao usar o @property (getter) e o @heuristica.setter, permite-nos tanto ler como alterar a função de estimativa de forma 
    controlada a partir de outras partes do código.
    """
 
    def __init__(self):
        self.__heuristica = None # heurística inicializada a None
    
    @property
    def heuristica(self): # getter
        return self.__heuristica
    
    @heuristica.setter
    def heuristica(self, heuristica): # setter
        self.__heuristica = heuristica