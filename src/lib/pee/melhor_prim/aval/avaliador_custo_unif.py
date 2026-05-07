from .avaliador import Avaliador

class AvaliadorCustoUnif(Avaliador):

    """
    A classe AvaliadorCustoUnif é o avaliador mais realista do nosso sistema.
    É usado pela Procura de Custo Uniforme e o seu método prioridade devolve simplesmente o custo real já acumulado desde o início 
    da exploração até ao nó atual (no.custo). 
    Não usa palpites nem estimativas do que falta: se um caminho custou 10 e o outro custou 15, o de 10 ganha prioridade máxima 
    na fronteira e é explorado primeiro, garantindo assim que encontramos sempre a solução com o menor esforço possível.
    """

    def prioridade(self, no):
        return no.custo # retornamos o custo do nó