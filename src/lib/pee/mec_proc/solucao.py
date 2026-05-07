from .passo_solucao import PassoSolucao

class Solucao:


    """
    A Solucao é o fim do algoritmo.
    Quando recebe o no objetivo (o no_final), o construtor faz o percurso inverso, salta de antecessor em antecessor até 
    ao no inicial, constroi gradualmente uma lista de objetos PassoSolucao que descreve exatamente que ações tomar. 
    Além de disponibilizar a dimensao (profundidade ou número de passos) e o custo total do trajeto, esta classe implementa 
    métodos do Python (__iter__ e __getitem__) que lhe permitem tratar a solução final como uma lista normal, 
    facilitando a sua leitura, iteração ou extração de passos específicos.
    """ 

    def __init__(self, no_final):
        self.__dimensao = no_final.profundidade
        self.__custo = no_final.custo
        self.__passos = [] # faltava o "s" em passos
        no = no_final # utilizamos a vareavel "no" no ciclo while mas a vareavel nao estava defenida, agr ja esta
        while no.antecessor: 
            passo = PassoSolucao(no.antecessor.estado, no.operador) 
            self.__passos.insert(0,passo) 
            no = no.antecessor 

    def __iter__(self): #iteravel 
        return iter(self.__passos)

    def __getitem__(self, index): # indexavel
        return self.__passos[index]


    @property
    def dimensao(self): # estava simensao em vez de dimensao
        return self.__dimensao
    
    @property
    def custo(self):
        return self.__custo
    



