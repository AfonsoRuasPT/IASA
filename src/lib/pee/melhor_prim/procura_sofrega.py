from .procura_informada import ProcuraInformada
from .aval.avaliador_sofrega import AvaliadorSofrega

class ProcuraSofrega(ProcuraInformada):


    """
    A classe ProcuraSofrega é um tipo de procura informada. 
    A única coisa que este código faz é inicializar a máquina de procura passando-lhe o AvaliadorSofrega. 
    Na prática, isto cria um algoritmo que olha apenas para a meta, tentando ir sempre pelo caminho que aparentemente o deixa mais
    próximo do objetivo final, esquecendo-se completamente de olhar para o custo que já gastou para lá chegar.
    """

    def __init__(self):
        super().__init__(AvaliadorSofrega())
