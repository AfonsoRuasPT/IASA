from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim):


    '''
    Reescreve procurar() para receber e atribuir a heurística ao avaliador antes de iniciar a exploração.
    ProcuraInformada herda de ProcuraMelhorPrim.
    '''

    """
    A classe ProcuraInformada serve de ponte entre a estrutura geral da procura melhor-primeiro e a utilização prática de 
    estimativas (heurísticas). 
    Ao contrário das procuras não informadas que só olham para o custo passado, esta classe redefine o método procurar para 
    receber e injetar um objeto heuristica diretamente no avaliador antes de arrancar com a exploração padrão. 
    Serve para estruturar algoritmos que vão tomar decisões misturando o que já gastaram com a previsão do que ainda vão gastar.
    """

    def procurar(self, problema, heuristica): # recebe o problema e a heurística concreta a usar nesta procura;  "heuristica" estava mal escrito
        self._avaliador.heuristica = heuristica # atribui a heurística no avaliador atravez do setter
        return super().procurar(problema) # invoca o algoritmo de procura de ProcuraMelhorPrim com a heurística já configurada ;   faltava o return