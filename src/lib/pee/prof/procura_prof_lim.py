from .procura_profundidade import ProcuraProfundidade

"""
A classe ProcuraProfLim tenta resolver os defeitos da procura em profundidade normal introduzindo um limite máximo de profundidade 
(prof_max). 
Na prática, o método de expansão verifica se a profundidade do nó atual ainda é menor que essse limite, se já o tiver atingido, 
devolve uma lista vazia e não gera mais sucessores. 
Este metodo de procura resolve o problema do ramo infinito, dado que só permite a procura em profundidade até uma certa profundidade 
defenina como default de 10 no nossso codigo.
"""

class ProcuraProfLim(ProcuraProfundidade):

    def procurar(self, problema, prof_max = 10):
        self.__prof_max = prof_max # atributo privado
        return super().procurar(problema)

    def _expandir(self, problema, no):
        return super()._expandir(problema, no) if no.profundidade < self.__prof_max else []  # utilizacao de operador ternario
                      # expandir ]e protected como defenido na class MecanismoProcura, faltava o "_" e, super()._expandir(...)