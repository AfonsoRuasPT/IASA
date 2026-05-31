from .mecanismo_procura import MecanismoProcura
 
'''
A Procura em Grafos estende a procura básica para lidar com grafos que têm ciclos: quando o espaço de estados tem transições
reversíveis, a procura em árvore pode expandir o mesmo estado infinitamente.
A solução é manter um dicionário _explorados que regista todos os estados já visitados, evitando reexpandir estados repetidos.
'''
 
class ProcuraGrafo(MecanismoProcura): # herda de MecanismoProcura; acrescenta memória de estados explorados para evitar ciclos
 
    '''
    ProcuraGrafo evita a reexpansão de estados já visitados mantendo um dicionário _explorados indexado por estado.
    Antes de inserir um nó na fronteira, _manter() verifica se o estado
    já foi explorado. _memorizar() só insere o nó se _manter() devolver True.
 
    ProcuraGrafo herda de MecanismoProcura (generalização).
    '''  
 
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
        super()._iniciar_memoria() # inicia a fronteira chamando o método da superclasse
        self._explorados = {} # dicionário {estado: No} indexado por Estado
 
    def _memorizar(self, no):
        if self._manter(no): # só memoriza o nó se for para manter, se não significa que o no ja esta memorizado
            self._explorados[no.estado] = no # regista o estado no dicionário de explorados antes de inserir na fronteira
            super()._memorizar(no) # chama _memorizar() que insere o nó na fronteira
 
    def _manter(self, no): # verifica se o estado ainda não foi explorado
        return no.estado not in self._explorados # devolve True se o estado é novo (não está no dicionário)