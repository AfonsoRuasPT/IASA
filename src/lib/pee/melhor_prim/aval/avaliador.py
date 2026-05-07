from abc import ABC, abstractmethod

class Avaliador(ABC):

    """
    A interface Avaliador serve como critério de avaliação de cada nó. 
    A sua única função é obrigar as subclasses a implementar o método de cálculo de prioridade, que dita a prioridade desse 
    nó na fronteira. 
    Dependendo do problema/metodo de procura/avaliação desejada, quem herdar esta classe pode calcular essa prioridade usando 
    os criterios que desejar, estes criterios podem ser custo, distancia ao alvo ect...
    """

    @abstractmethod
    def prioridade(self, no):
        """Metodo abstrato que deve ser concretizado na subclass e deve implementar um criterio que define a prioridade de um nó"""
