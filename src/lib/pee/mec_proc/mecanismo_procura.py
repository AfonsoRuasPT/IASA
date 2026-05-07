from .no import No
from .solucao import Solucao

class MecanismoProcura:

    """
    O MecanismoProcura é o que faz a exploração do espaco de estados, utilizando a fronteira fornecida para guiar a sua navegação.
    O seu metodo central é o procurar, que a partir do estado inicial e a sua expanção atravez de operadores retorna ou não uma solução.
    """

    def __init__(self, fronteira):
        self._fronteira = fronteira

    def _iniciar_memoria(self): # inincia a fronteira
        self._fronteira.iniciar()

    def _memorizar(self, no):  # inserir no na fronteira
        self._fronteira.inserir(no)

    def procurar(self, problema): # retorna uma solucao
        self._iniciar_memoria()             # iniciamos a memoria do mecanismo de procura
        no = No(problema.estado_inicial)    # criamos o no inicial do problema, ponto de partida, o nó inicial é um propriedade do problema, logo basta chamar o getter
        self._memorizar(no)                 # memorizamos o no inicial
        while not self._fronteira.vazia:    # verificamos se a fronteira nao esta vazia, porque se/quando estiver significa que o 
                                            # problema nao tem solucao ou que nao encontramos nenhuma solucao que nos satisfaça, isto 
                                            # pode acontecer se o nosso criterio de solucao so aceitar solucoes com custo inferior a 
                                            # 1000 e tedas as "solucoes" encontradas tiverem custos superiores, por exemplo

            no = self._fronteira.remover() # uma vez que a fronteira nao esta vazia retiramos o no da fronteira segundo o criterio de remoção, que pode ser vareado, de largura ou em prefundidade
            if problema.objectivo(no.estado): # se o estado associado ao no for o objetivo do problema que aceitamos retornamos a solucao
                return Solucao(no)
            for no_suc in self._expandir(problema, no): # expandimos o nosso no, ou seja, geramos nos sucessores aplicando operadores ao nosso no
                self._memorizar(no_suc)                 # adicionamose esses nos a memoria do mecanismo de procura



    def _expandir(self, problema, no): # retorna uma lista de nos
        sucessores = []                # iniciamos uma lista de nos vazios
        estado = no.estado             # guardamos o estado do no na vareavel estado, para eficiencia e legibilidade
        for operador in problema.operadores: # iteramos obre os operadores do problema, que é uma propriedade do problema, logo basta chamar o getter
            estado_suc = operador.aplicar(estado) #aplicamos o operador ao nosso no, criando o estado sucessor
            if estado_suc is not None: # se o estado sucessor nao for nulo
                custo = no.custo + operador.custo(estado, estado_suc) # calculamos o custo deste no_sucessor, que é a soma do custo do no atual com o custo de aplicar o eperador ao estado do no atual
                no_suc = No(estado_suc, operador, no, custo) # criamos o no sucessor, associando-lhe o estado sucessor, o operador, o no pai e o custo
                sucessores.append(no_suc) # adicionamos o no sucessor a lista de nos sucessores
        return sucessores # depois de iterar sobre todos os operadores retornamos a lista de nos sucessores
