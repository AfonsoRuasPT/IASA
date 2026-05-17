from agente.controlo import Controlo
from .mec_delib import MecDelib
from .modelo.modelo_mundo import ModeloMundo
import sae

class ControloDelib(Controlo):

    """
    O ControloDelib implementa o ciclo de vida do agente deliberativo. De acordo com o diagrama 
    da arquitetura, esta classe atua como o orquestrador principal, ligando a perceção do 
    ambiente à ação através de simulação interna. Gere o ModeloMundo para manter a 
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

    def processar(self, percepcao): # fiz este metodo com o diagrama de atividades na parte 4 slide 6
        percepcao = self.__assimilar(percepcao) # atualizamos o modelo do mundo com a percepcao recebida
        if self.__reconsiderar(): # verificamos de reconsideramos os objectivos
            self.__deliberar() # deliberamos
            self.__planear() # planeamos
        accao = self.__executar() 
        return accao # retornamos a acção executar

    def __assimilar(self, percepcao):
        """
        Atualização o estado interno da classe ModeloMundo, passando a 
        perceção recebida como argumento para o método atcualizar do modelo.
        """
        self.__modelo_mundo.actualizar(percepcao) 

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
        if self.__objectivos:
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)
        else:
            self.__plano = None
        # se existirem objectivos, entao planear, caso contrario nao existe plano

    def __executar(self):
            self.__mostrar()
            if self.__plano:
                estado = self.__modelo_mundo.obter_estado()
                operador = self.__plano.obter_accao(estado)
                if operador:
                    return operador.accao
                else:
                    self.__plano = None

    def __mostrar(self):
            sae.vista.limpar()
            self.__modelo_mundo.mostrar(sae.vista)
            if self.__plano:
                self.__plano.mostrar(sae.vista)
            if self.__objectivos:
                for objectivo in self.__objectivos:
                    sae.vista.marcar_posicao(objectivo.posicao)

