from .mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura):


    """
    A classe ProcuraGrafo é uma evolução direta do mecanismo de procura base, desenhada especificamente para lidar com problemas 
    onde o espaço de estados tem ciclos (ou seja, quando existem caminhos que nos levam de volta a situações por onde já passámos).
    O método _iniciar_memoria prepara o terreno para esta nova mecânica: além de iniciar a fronteira normal aproveitando o código
    da superclasse, cria um dicionário vazio chamado _explorados. Este dicionário vai funcionar como a memória histórica do 
    algoritmo para registar e indexar todos os estados visitados, garantindo um acesso rápido. 
    O método _manter serve como um filtro de admissão que verifica simplesmente se o estado do nó atual já existe na nossa 
    memória de _explorados. 
    Finalmente, o método _memorizar aplica este filtro: antes de atirar um nó recém-gerado para a 
    fila de espera (fronteira), pergunta ao _manter se o devemos reter. Se o estado for efetivamente novo, guarda-o 
    imediatamente no dicionário de explorados e só depois chama a superclasse para o colocar na fronteira. Na prática, 
    esta classe é fundamental para impedir que o algoritmo fique preso em ciclos infinitos ou desperdice tempo e memória a 
    expandir estados repetidos.
    """  

    def _iniciar_memoria(self):
        super()._iniciar_memoria() # invocar o iniciar memoria da super class para iniciar a fronteira
        self._explorados = {} # inicia o dicionario vazio dos explorados
        
    def _memorizar(self, no):
        # se for para manter o no, 
        if self._manter(no):
            self._explorados[no.estado] = no
            super()._memorizar(no)

    def _manter(self, no):
        return no.estado not in self._explorados