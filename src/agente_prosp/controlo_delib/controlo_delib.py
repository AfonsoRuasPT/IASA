from agente.controlo import Controlo
from .mec_delib import MecDelib
from .modelo.modelo_mundo import ModeloMundo

class ControloDelib(Controlo):

    """
    O ControloDelib implementa o ciclo de vida do agente deliberativo. De acordo com o diagrama 
    da arquitetura, esta classe atua como o orquestrador principal, ligando a perceção do 
    ambiente à ação através de simulação interna. Ela gere o ModeloMundo para manter a 
    representação do estado, o MecDelib para decidir os objetivos a atingir e o Planeador 
    para calcular os caminhos até esses objetivos.
    """

    def __init__(self, planeador):

        """
        Construtor da classe ControloDelib. 
        Internamente, constrói a representação do mundo
        instanciando o ModeloMundo e inicializa o mecanismo de deliberação MecDelib passando-lhe
        a referência deste modelo.
        """
        
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo() # criar instancia de modelo mundo
        self.__mec_delib = MecDelib(self.__modelo_mundo) # instanciar MecDelib com o self.__modelo_mundo
        self.__objectivos = [] # iniciar objectivos como uma lista vazia, inicialmente não ah objectivos
        self.__plano = None

    def processar(self, percepcao):
        pass

    def __assimilar(self, percepcao):
        """
        Atualização o estado interno da classe ModeloMundo, passando a 
        perceção recebida como argumento para o método atcualizar do modelo.
        """
        self.modelo_mundo.actualizar(percepcao) 

    def __reconsiderar(self):
        """
        Segundo a arquitetura esta decisão apoia-se na propriedade de leitura alterado do ModeloMundo, 
        que indica se a última perceção modificou significativamente a representação interna 
        do ambiente, ou na ausência de um plano atual.
        """
        return self.__modelo_mundo.alterado or not self.__plano 
        # reconsideramos se o modelo do mundo tiver sido alterado ou se nao existir plano

    def __deliberar(self):

        """
        Invoca o mecanismo de deliberação para atualizar a lista de objetivos. Esta chamada 
        ao método deliberar do MecDelib retorna uma lista de instâncias de EstadoAgente 
        que representam os destinos pretendidos.
        """

        self.__objectivos = self.__mec_delib.deliberar()

    def __planear(self):
        self.__planeador.planear()

    def __executar(self):

    def __mostrar(self):