from abc import abstractmethod

class Fronteira:

    """
    A Fronteira gere a lista de nós que já foram descobertos, mas que ainda aguardam a sua vez para serem explorados. 
    O metodo iniciar lista vazia ou seja o inicio da fronteira, e o metodo abstrato inserir
    dita a regra de entrada, é esta regra que define se os nós entram para o fim (LIFO) ou para o início (FIFO) da fila,
    o que determina se a procura é feita em largura ou em profundidade. 
    
    O metodo remover retira e devolve o primeiro nó da fila para ser analisado, e a propriedade vazia informa o sistema se 
    ainda existem caminhos disponiveis para explorar ou se todas as opções ja se esgotaram.
    """

    def __init__(self):
        self.iniciar()

    def iniciar(self):
        self._nos = [] # inicia uma lista de nos vazia

    @abstractmethod
    def inserir(self, no):
        """"""

    def remover(self): # remove o no na posicao 0 da fronteira
        return self._nos.pop(0)
    
    @property
    def vazia(self):
        return len(self._nos) == 0
    # propriedade privada em que o valor retornado é dinamucamente calculado