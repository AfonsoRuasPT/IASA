"""
Plataforma SAE - Simulador de ambiente de execução
@author: Luís Morgado
"""

#__________________________________________________
vista = None
"""Vista de visaualização do modelo"""
transdutor = None
"""Transdutor de interacção com o ambiente"""

#__________________________________________________
# Definições públicas

from .simulador import Simulador
from .agente.movimento import Movimento
from .ambiente.elemento import Elemento
from .ambiente.direccao import Direccao
