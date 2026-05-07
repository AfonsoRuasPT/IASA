class No:

    """
        A classe No é a estrutura de dados fundamental que constrói a arvore de procura, estrutura  onde é possivel visualizar todos 
        os nós e os seus nos sucessores e antecessores desde o no inicial. 
        Cada nó memoriza o seu estado atual e o seu no antecessor, a ação que lhe deu origem (operador), a que profundidade se encontra 
        (calculada automaticamente somando 1 à profundidade do no antecessor) e o custo acumulado até esse ponto. Adicionalmente, esta 
        classe introduz uma prioridade e um método de comparação (__lt__) que permite comparar objetos (self < outro) e ordenar listas 
        desta classe.
    """

    def __init__(self, estado, operador = None, antecessor = None, custo = 0):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo
        self.__prioridade = 0
        if antecessor:
            self.__profundidade = antecessor.profundidade + 1
        else:
            self.__profundidade = 0


    def __lt__(self, no):
        return self.prioridade < no.prioridade

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
