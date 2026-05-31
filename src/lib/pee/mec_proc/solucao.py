from .passo_solucao import PassoSolucao
 
'''
A Solução (slide 30 Parte3) representa o percurso no espaço de estados
que liga o estado inicial ao estado objectivo: a sequência ordenada de
estados e operadores que resolve o problema.
É construída a partir do nó objectivo percorrendo a cadeia de antecessores
até à raiz (nó inicial), reconstruindo o percurso em sentido inverso.
'''
 
class Solucao:
 
    '''
    Solucao encapsula o percurso solução encontrado pelo mecanismo de procura. 
    Reconstrói a sequência de passos a partir do nó final, seguindo a cadeia de antecessores até à raiz. 
    Expõe a dimensão (número de passos), o custo total e permite iterar ou indexar os passos.
 
    Solucao é composta por PassoSolucao, cada passo guarda o estado e o operador.
    '''
 
    """
    A Solucao é o fim do algoritmo.
    Quando recebe o no objetivo (o no_final), o construtor faz o percurso inverso, salta de antecessor em antecessor até 
    ao no inicial, constroi gradualmente uma lista de objetos PassoSolucao que descreve exatamente que ações tomar. 
    Além de disponibilizar a dimensao (profundidade ou número de passos) e o custo total do trajeto, esta classe implementa 
    métodos do Python (__iter__ e __getitem__) que lhe permitem tratar a solução final como uma lista normal, 
    facilitando a sua leitura, iteração ou extração de passos específicos.
    """ 
 
    def __init__(self, no_final): # recebe o nó objectivo encontrado pelo mecanismo de procura
        self.__dimensao = no_final.profundidade # número de passos da solução (profundidade do nó final)
        self.__custo = no_final.custo # custo total acumulado desde a raiz até ao nó final
        self.__passos = []
        no = no_final # variável de iteração que percorre a cadeia de antecessores
        while no.antecessor: # percorre de trás para a frente até ao nó raiz
            passo = PassoSolucao(no.antecessor.estado, no.operador) # cria um passo com o estado do antecessor e o operador que gerou o nó actual
            self.__passos.insert(0, passo) # insere no início para manter a ordem cronológica (raiz - objectivo)
            no = no.antecessor # avança para o nó antecessor
 
    def __iter__(self): #  torna Solucao iterável
        return iter(self.__passos) 
 
    def __getitem__(self, index): # torna Solucao indexável
        return self.__passos[index] # acesso directo ao passo pelo índice
 
    @property
    def dimensao(self): # número de passos da solução 
        return self.__dimensao
    
    @property
    def custo(self): # custo total da solução
        return self.__custo