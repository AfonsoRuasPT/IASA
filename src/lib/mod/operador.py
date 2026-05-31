from abc import ABC, abstractmethod

'''
Os Operadores representam as acções que produzem a mudança (transformação) de estado no espaço de estados.
Operam sobre as representações internas de estado, produzindo transições de estado que correspondem à geração de novos estados.
São o mecanismo que permite ao algoritmo de procura simular internamente o efeito de cada acção possível sem a executar fisicamente.
'''

class Operador(ABC): # interface que define o contrato de qualquer operador de transição de estado

    '''
    Operador define o contrato de qualquer acção que transforma estados. 
    Qualquer operador concreto deve implementar:
      aplicar(estado) - novo estado resultanta da acção
      custo(estado, estado_suc) - custo da transição


    Operador é agregado por Problema.
    '''

    """
    A classe Operador representa a abstração das ações que provocam a mudança do espaço de estados, o transforma o estado "a" no estado "a+1".

    O método aplicar aplica o operador ao estado atual, executa a ação pretendida sobre o estado e devolve um estado inteiramente novo que resulta dessa transformação. 
    Adicionalmente, o método custo existe para quantificar o "preço computacional/energetico", a distância ou o esforço necessário para transitar de um estado para o estado 
    sucessor gerado pela ação. 
    Estes métodos são abstratos porque a forma como uma ação se aplica e o seu custo é calculado depende sempre da natureza específica do problema e do tipo de operador aplicado
    """

    @abstractmethod
    def aplicar(self, estado): # dado um estado actual, devolve o estado sucessor resultante da acção 
        """"""

    @abstractmethod
    def custo(self, estado, estado_suc): # devolve o custo da transição entre estado e estado_suc
        """"""