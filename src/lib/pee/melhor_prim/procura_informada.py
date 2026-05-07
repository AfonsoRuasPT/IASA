from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim):

    """
    A classe ProcuraInformada serve de ponte entre a estrutura geral da procura melhor-primeiro e a utilização prática de 
    estimativas (heurísticas). 
    Ao contrário das procuras não informadas que só olham para o custo passado, esta classe redefine o método procurar para 
    receber e injetar um objeto heuristica diretamente no avaliador antes de arrancar com a exploração padrão. 
    Serve para estruturar algoritmos que vão tomar decisões misturando o que já gastaram com a previsão do que ainda vão gastar.
    """

    def procurar(self, problema, heuristica): # "heuristica" estava mal escrito
        self._avaliador.heuristica = heuristica
        return super().procurar(problema) # faltava o return