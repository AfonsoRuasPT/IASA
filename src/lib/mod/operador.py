from abc import ABC, abstractmethod

class Operador(ABC):

    """
    A classe Operador representa a abstração das ações que provocam a mudança do espaço 
    de estados, o transforma o estado a no estado a+1.

    O método aplicar aplica o operador ao estado atual, executa a ação pretendida 
    sobre ele e devolve um estado inteiramente novo que resulta dessa transformação. 
    Adicionalmente, o método custo existe para quantificar o "preço computacional/energetico", 
    a distância ou o esforço necessário para transitar de um estado para o estado 
    sucessor gerado pela ação. 
    Estes métodos são abstratos porque a forma como uma ação se aplica e o seu custo
    é calculado depende sempre da natureza específica do problema e do tipo de operador aplicado
    """

    @abstractmethod
    def aplicar(self, estado):
        """"""

    @abstractmethod
    def custo(self, estado, estado_suc):
        """"""