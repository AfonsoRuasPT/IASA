"""
Movimento do agente
@author: Luís Morgado
"""

from dataclasses import dataclass

from ..ambiente.direccao import Direccao

#_______________________________________________________________________________

@dataclass
class Movimento:
    """Representação de movimento de actuação"""
    direccao: Direccao
    """Direcção de movimento"""
    passo: int = 1
    """Distância de movimento"""

    @property
    def ang(self):
        """
        Ângulo da direcção da movimento
        """
        return self.direccao.value

    def __hash__(self):
        """
        Identificação por valor
        """
        return hash(self.direccao)    
  
    def __repr__(self):
        """
        Representação de movimento
        """
        return f"Movimento: direcção={self.direccao}, passo={self.passo}"

    def mostrar(self):
        """
        Mostrar movimento
        """
        print(self)
