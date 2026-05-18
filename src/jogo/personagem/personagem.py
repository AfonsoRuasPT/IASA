from agente.agente_jogo import AgenteJogo
from .controlo_personagem import ControloPersonagem


class Personagem(AgenteJogo): # herda de AgenteJogo, especialização do agente para o contexto do jogo

    '''
    Personagem é uma especialização final de AgenteJogo que é especialização de Agente.
    É o agente autónomo e reactivo que procura e fotografa animais.

    
    Herde de AgenteJogo e tem relação de dependencia com AmbienteJogo e ControloPersonagem
    '''

    def __init__(self, ambiente): # recebe ambiente como parametro
        super().__init__(ambiente, ControloPersonagem()) # invoca o construtor de AgenteJogo passando o ambiente e uma nova instância de ControloPersonagem
    
    def mostrar(self): # imprime o estado actual da personagem
      #  print(f"\nPersonagem: {self._controlo.__maq_est.estado_atual.name}") Antes tinha isto
      print(f"\nEstado: {self._controlo.estado.name}") # acede ao estado via a propriedade pública estado de ControloPersonagem