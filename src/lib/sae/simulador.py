"""
Simulador de ambiente com visualização gráfica
@author: Luís Morgado
"""

import sae

from .defamb import DEF_AMB
from .erro import Erro, erro_terminar, NOME_EXEC
from .ambiente.ambiente import Ambiente
from .vistas.vista_simul import VistaSimul
from .modelo.modelo_simul import ModeloSimul
from .controlador.controlador_simul import ControladorSimul
from .plataforma.aplicacao import Aplicacao
from .agente.transdutor import Transdutor

#_____________________________________________________________

# Configuração por omissão
TEMPO_PASSO = 100 # ms
"""Tempo do passo de execução"""
TEMPO_VMAX = 10 # ms
"""Tempo do passo de execução com velocidade máxima"""

#_____________________________________________________________

class Simulador:
    def __init__(self, num_amb, agente, reiniciar=False, vista_modelo=False):
        """
        Iniciar simulador
        @param num_amb: número do ambiente
        @param agente: agente a executar
        @param reiniciar: reiniciar automático da simulação com recolha de alvo
        @param vista_modelo: mostrar vista do modelo interno do agente
        """
        # Iniciar ambiente
        self.__ambiente = self.__iniciar_ambiente(num_amb)
        # Iniciar transdutor de interacção com o ambiente
        sae.transdutor = Transdutor(self.__ambiente)
        # Iniciar aplicação
        self.__aplicacao = Aplicacao()
        # Iniciar modelo de simulação
        if self.__executavel(agente):
            self.__modelo = ModeloSimul(self.__ambiente, agente, reiniciar)
        else:
            erro_terminar(Erro.AGENTE_NAO_EXEC, agente.__class__.__name__)
        # Iniciar vista de simulação
        self.__vista = VistaSimul(self.__aplicacao, self.__modelo, vista_modelo)
        # Iniciar controlador de simulação
        self.__controlador = ControladorSimul(self.__vista, self.__modelo)
        # iniciar vista de visualização do modelo
        sae.vista = self.__vista.vista_modelo

    def __executavel(self, agente):
        """Verifica se uma instância de agente é executável"""
        if hasattr(agente, NOME_EXEC):
            atrib_exec = getattr(agente, NOME_EXEC)
            return callable(atrib_exec)
    
    def __iniciar_ambiente(self, num_amb):
        """
        Obter definição de ambiente
        @param num_amb: número do ambiente
        @return: ambiente
        """
        if num_amb in DEF_AMB:
            return Ambiente(DEF_AMB[num_amb])
        else:
            erro_terminar(Erro.AMB_NAO_DEF, num_amb)

    def executar(self):
        """
        Executar simulação
        """
        # Iniciar aplicação com controlador de execução da simulação
        self.__aplicacao.iniciar(self.__controlador, TEMPO_PASSO, TEMPO_VMAX)


        
