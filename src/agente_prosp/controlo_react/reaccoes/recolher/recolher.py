from ecr.hierarquia import Hierarquia
from ..explorar.explorar import Explorar
from ..explorar.explorar_mem import ExplorarMem
from ..aproximar.aproximar_alvo import AproximarAlvo
from ..evitar.evitar_obst import EvitarObst

class Recolher(Hierarquia):

    """
    Recolher é um comportamento composto, cuja selecao de accao é feita de forma hierarquica.
    Este comportamento composto, é composto por 3 comportamentos: AproximarAlvo, EviarObst, Explorar.
    A hierarquia de cad acomportamento está descrito em cada um deles
    """

    """
    Este comportamento composto descreve todos os comportamentos do nosso agente, dado que é composto por outros comportamentos/comportamente compostos.
    
    """

    def __init__(self):
        super().__init__((AproximarAlvo(), EvitarObst(), ExplorarMem(), Explorar())) # AproximarAlvo(), EvitarObst(), ExplorarMem(), 