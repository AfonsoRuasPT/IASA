from agente.controlo import Controlo
from .mec_delib import MecDelib
from .modelo.modelo_mundo import ModeloMundo
import sae

'''
O Controlo Deliberativo é o módulo que organiza de forma modular o Modelo do Mundo, o Mecanismo de Deliberação e o Planeador.
Coordena o ciclo de tomada de decisão e acção:
  1 - Assimilar a percepção 
  2 - Reconsiderar 
  3 - Deliberar
  4 - Planear
  5 - Executar
'''

class ControloDelib(Controlo):

    def __init__(self, planeador):

        """
        ControloDelib é o orquestrador do ciclo deliberativo do agente.
        Implementa o contrato da interface Controlo que cordena o ModeloMundo, o MecDelib e o Planeador para produzir a acção a executar 
        em cada ciclo.
 
        ControloDelib realiza Controlo.
        ControloDelib compõe ModeloMundo.
        ControloDelib compõe MecDelib.
        ControloDelib tem uma associação com Planeador.
        """
        
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo() # criar instancia de modelo mundo
        self.__mec_delib = MecDelib(self.__modelo_mundo) # instanciar MecDelib com o self.__modelo_mundo
        self.__objectivos = [] # iniciar objectivos como uma lista vazia, inicialmente não ah objectivos
        self.__plano = None

    def processar(self, percepcao): # fiz este metodo com o diagrama de atividades na parte 4 slide 6
        # implementação do método abstracto de Controlo
        percepcao = self.__assimilar(percepcao) # atualizamos o modelo do mundo com a percepcao recebida
        if self.__reconsiderar(): # verificamos de reconsideramos os objectivos
            self.__deliberar() # deliberamos
            self.__planear() # planeamos
        accao = self.__executar() 
        return accao # retornamos a acção executar

    def __assimilar(self, percepcao):
        """
        Actualiza o estado interno do ModeloMundo com a percepção recebida,
        correspondendo ao passo 1 do ciclo deliberativo.
        """
        self.__modelo_mundo.actualizar(percepcao) #a actualiza o ModeloMundo consoante a percepcao percepção

    def __reconsiderar(self):
        """
        Decide se é necessário redeliberar e replanear, passo 2 do ciclo.
        Reconsiderar é necessário quando o ambiente muda ou quando não existe plano válido.
        Evita deliberar e planear desnecessariamente quando o ambiente não mudou e o plano ainda é válido.
        """
        return self.__modelo_mundo.alterado or not self.__plano 
        # reconsideramos se o modelo do mundo tiver sido alterado ou se nao existir plano

    def __deliberar(self):

        """
        Invoca o MecDelib para gerar a lista de objectivos, passo 3 do ciclo.
        Corresponde ao raciocínio que decide o que fazer.
        """

        self.__objectivos = self.__mec_delib.deliberar()

    def __planear(self):
        # gera um novo plano para os objectivos actuais, passo 4 do ciclo.
        if self.__objectivos: # se existirem objectivos
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos) # planeia sobre o modelo_mundo consoante ob objectivos
        else: # se não existirem objectivos
            self.__plano = None # não existe plano
        # se existirem objectivos, entao planear, caso contrario nao existe plano

    def __executar(self):
            self.__mostrar() # actualiza a visualização
            if self.__plano: # se existir plano 
                estado = self.__modelo_mundo.obter_estado() # obtém o estado actual do agente
                operador = self.__plano.obter_accao(estado) # obtém o operador correspondente ao estado actual no plano
                if operador: # se o plano devolveu um operador válido para este estado
                    return operador.accao # devolve a acção Mover ao agente
                else: # se não
                    self.__plano = None # o plano está dessincronizado com o estado actual e não exisste plano

    def __mostrar(self): # actualiza a visualização gráfica
            sae.vista.limpar() # limpa o ecran
            self.__modelo_mundo.mostrar(sae.vista) # mostra o modelo mundo
            if self.__plano: # se existir plano
                self.__plano.mostrar(sae.vista) # mostra o plano
            if self.__objectivos: # se existir objectivos
                for objectivo in self.__objectivos:
                    sae.vista.marcar_posicao(objectivo.posicao) # mostra o objectivo marcado

