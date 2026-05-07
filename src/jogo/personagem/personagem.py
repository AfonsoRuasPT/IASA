from agente.agente_jogo import AgenteJogo
from .controlo_personagem import ControloPersonagem


class Personagem(AgenteJogo):

    def __init__(self, ambiente):
        super().__init__(ambiente, ControloPersonagem()) 
    
    def mostrar(self):
      #  print(f"\nPersonagem: {self._controlo.__maq_est.estado_atual.name}") Antes tinha isto
      print(f"\nEstado: {self._controlo.estado.name}")