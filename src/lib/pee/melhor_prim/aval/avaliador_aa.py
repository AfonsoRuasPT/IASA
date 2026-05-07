from .avaliador_heur import AvaliadorHeur

class AvaliadorAA(AvaliadorHeur):

    """
    A classe AvaliadorAA é o motor de decisão responsável pelo algoritmo de procura A*.
    O seu método prioridade utiliza o custo real que já gastámos para chegar até àquele nó (no.custo) e soma-lhe a estimativa do 
    que ainda falta percorrer até ao objetivo, calculada pela heurística (self.heuristica.h(no.estado)). 
    Na teoria da Inteligência Artificial, isto corresponde à fórmula clássica f(n) = g(n) + h(n).
    Ao somar o esforço passado com a previsão futura, este avaliador garante que o algoritmo não é demasiado "cego" 
    (como a Procura de Custo Uniforme, que só olha para trás) nem demasiado "precipitado" (como a Procura Sófrega, que só olha 
    para a frente). 
    É este equilíbrio exato que permite ao A* ser simultaneamente eficiente e capaz de garantir que encontra sempre o melhor 
    caminho possível.
    """

    def prioridade(self, no):
        return self.heuristica.h(no.estado) + no.custo # f(n) = h(n) (heuristica) + g(h) (custo do nó)