from .procura_profundidade import ProcuraProfundidade
 
'''
A Procura em Profundidade Limitada Depth-Limited Search resolve o problema dos ramos infinitos da procura em profundidade introduzindo
um limite máximo de profundidade. 
Quando um nó atinge o limite, não expande mais sucessores, obrigando o algoritmo a recuar.
Problema - se a solução estiver a uma profundidade superior ao limite, não é encontrada.
'''
 
class ProcuraProfLim(ProcuraProfundidade): # herda de ProcuraProfundidade
 
    '''
    ProcuraProfLim limita a procura em profundidade a prof_max níveis.
    Sobrepõe _expandir() para devolver lista vazia quando o nó atingiu o limite, impedindo a expansão de ramos mais profundos.
 
    ProcuraProfLim herda de ProcuraProfundidade.
    '''
 
    """
    A classe ProcuraProfLim tenta resolver os defeitos da procura em profundidade normal introduzindo um limite máximo de profundidade (prof_max). 
    Na prática, o método de expansão verifica se a profundidade do nó atual ainda é menor que essse limite, se já o tiver atingido, 
    devolve uma lista vazia e não gera mais sucessores. 
    Este metodo de procura resolve o problema do ramo infinito, dado que só permite a procura em profundidade até uma certa profundidade 
    defenina como default de 10 no nossso codigo.
    """
 
    def procurar(self, problema, prof_max = 10): # recebe o problema e o limite de profundidade (default 10)
        self.__prof_max = prof_max # guarda o limite de profundidade para uso em _expandir()
        return super().procurar(problema) # invoca o algoritmo de procura da superclasse com o limite configurado
 
    def _expandir(self, problema, no): # sobrepõe _expandir, só expande se a profundidade do nó for inferior ao limite
        return super()._expandir(problema, no) if no.profundidade < self.__prof_max else [] # operador ternário, expande normalmente ou devolve lista vazia se limite for atingido