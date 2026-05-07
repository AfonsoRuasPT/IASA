from .procura_informada import ProcuraInformada
from .aval.avaliador_aa import AvaliadorAA

class ProcuraAA(ProcuraInformada):

    """
    A classe ProcuraAA implementa o algoritmo de procura A*. 
    Herda da ProcuraInformada é muito simples porque a sua única tarefa é arrancar 
    inicializando o AvaliadorAA. 
    Este avaliador específico encarrega-se da matemática por trás do A*: classificar e dar prioridade aos nós somando o custo real
    já percorrido com o valor devolvido pela heurística.
    """

    def __init__(self):
        super().__init__(AvaliadorAA())