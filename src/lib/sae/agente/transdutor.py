"""
Transdutor de percepção e actuação
@author: Luís Morgado
"""

from ..ambiente.elemento import Elemento
from .percepcao import Percepcao

#_______________________________________________________________________________

class Transdutor:
    """
    Transdutor geral de interacção com um ambiente
    """
    def __init__(self, ambiente=None):
        if ambiente:
            self.iniciar(ambiente)

    @property
    def ambiente(self):
        return self._ambiente

    def iniciar(self, ambiente):
        """Iniciar transdutor definindo o ambiente associado"""
        self._ambiente = ambiente
        
    def percepcionar(self):
        """
        Percepcionar ambiente
        @return: percepção
        """
        items_ambiente = self._ambiente.elementos.items()

        posicoes = [pos for pos, elem in items_ambiente
                    if elem != Elemento.OBSTACULO]

        elementos = {pos: elem for pos, elem in items_ambiente
                     if elem in [Elemento.ALVO, Elemento.OBSTACULO]}

        return Percepcao(
					self._ambiente.per_dir,
					self._ambiente.posicao_agente,
					self._ambiente.direccao_agente,
					posicoes,
					elementos,
					self._ambiente.recolha,
					self._ambiente.colisao
				)

    def actuar(self, movimento):
        """
        Activar actuador com o movimento
        @param movimento: movimento a executar
        """
        if movimento:
            if movimento.passo > 0:
                self._ambiente.mover_agente(movimento.direccao)
            else:
                self._ambiente.rodar_agente(movimento.direccao)
                
