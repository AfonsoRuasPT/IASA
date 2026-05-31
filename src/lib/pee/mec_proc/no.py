'''
A Árvore de Procura é a estrutura que mantém a informação gerada em cada passo de procura. 
É organizada em nós que relacionam cada estado explorado com o seu antecessor e com o operador que originou a
transição. Permite reconstruir o percurso solução a partir do nó objectivo.
Cada nó mantém:
  Estado      - a configuração do problema neste ponto
  Operador    - a acção que gerou este estado
  Antecessor  - o nó pai na árvore
  Profundidade- distância ao nó inicial
  Custo       - custo acumulado desde a raiz até este nó
'''

class No:

    '''
    No é a unidade estrutural da árvore de procura.
    Cada nó encapsula um estado, o operador que o gerou, o nó antecessor e a informação de profundidade e custo necessária para controlar a procura.

    No é composto por Estado.
    No tem uma associação recursiva com No.
    No tem uma associação com Operador.
    '''

    """
        A classe No é a estrutura de dados fundamental que constrói a arvore de procura, estrutura  onde é possivel visualizar todos 
        os nós e os seus nos sucessores e antecessores desde o no inicial. 
        Cada nó memoriza o seu estado atual e o seu no antecessor, a ação que lhe deu origem (operador), a que profundidade se encontra 
        (calculada automaticamente somando 1 à profundidade do no antecessor) e o custo acumulado até esse ponto. Adicionalmente, esta 
        classe introduz uma prioridade e um método de comparação (__lt__) que permite comparar objetos (self < outro) e ordenar listas 
        desta classe.
    """

    def __init__(self, estado, operador = None, antecessor = None, custo = 0):
        self.__estado = estado # estado associado a este nó
        self.__operador = operador # operador que gerou este nó 
        self.__antecessor = antecessor # nó pai na árvore de procura 
        self.__custo = custo # custo acumulado desde a raiz até este nó
        self.__prioridade = 0 # prioridade de expansão na FronteiraPrioridade
        if antecessor: # se existe antecessor, a profundidade é a do antecessor + 1
            self.__profundidade = antecessor.profundidade + 1
        else: # nó raiz: profundidade 0
            self.__profundidade = 0

    def __lt__(self, no): # método especial invocado pelo operador "<" 
        return self.prioridade < no.prioridade # compara nós pela prioridade

    @property
    def profundidade(self): 
        return self.__profundidade 
    
    @property
    def custo(self):
        return self.__custo
    
    @property
    def prioridade(self): 
        return self.__prioridade
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador
    
    @prioridade.setter
    def prioridade(self, valor):
        self.__prioridade = valor
    
    @property
    def antecessor(self):
        return self.__antecessor