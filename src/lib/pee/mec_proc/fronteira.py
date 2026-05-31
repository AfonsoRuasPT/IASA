from abc import abstractmethod
 
'''
A Fronteira de Exploração é a estrutura de dados que mantém os nós gerados mas ainda não expandidos (nós abertos).
O critério de ordenação da fronteira determina a estratégia de controlo da procura:, qual o próximo nó a expandir.
  LIFO  - Procura em Profundidade: expande os nós mais recentes
  FIFO  - Procura em Largura: expande os nós mais antigos
  Prioridade  - Melhor-Primeiro: expande o nó com menor f(n)
'''
 
class Fronteira: # classe base que define o contrato e comportamento comum de qualquer fronteira de exploração
 
    '''
    Fronteira define o contrato e o comportamento base de gestão dos nós por expandir. 
    O método abstracto inserir() define onde cada subclasse insere o nó na lista, o que determina a estratégia de exploração.
 
    Fronteira é realizada por FronteiraLIFO, FronteiraFIFO e FronteiraPrioridade.
    É composta por MecanismoProcura.
    '''
 
    """
    A Fronteira gere a lista de nós que já foram descobertos, mas que ainda aguardam a sua vez para serem explorados. 
    O metodo iniciar lista vazia ou seja o inicio da fronteira, e o metodo abstrato inserir
    dita a regra de entrada, é esta regra que define se os nós entram para o fim (LIFO) ou para o início (FIFO) da fila,
    o que determina se a procura é feita em largura ou em profundidade. 
    
    O metodo remover retira e devolve o primeiro nó da fila para ser analisado, e a propriedade vazia informa o sistema se 
    ainda existem caminhos disponiveis para explorar ou se todas as opções ja se esgotaram.
    """
 
    def __init__(self):
        self.iniciar() # inicia a fronteira vazia ao criar a instância
 
    def iniciar(self): # reinicia a fronteira eliminando todos os nós
        self._nos = [] #  atributo protegido acessível nas subclasses, inicia a lista de nós vazia
 
    @abstractmethod
    def inserir(self, no): # define onde o nó entra na lista (início=LIFO, fim=FIFO, heap=prioridade)
        """"""
 
    def remover(self): # remove e devolve o primeiro nó da lista
        return self._nos.pop(0) # pop(0) remove e devolve o elemento na posição 0 (o próximo a expandir)
    
    @property
    def vazia(self): # devolve True se não há nós por expandir
        return len(self._nos) == 0