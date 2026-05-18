from enum import Enum

class EstadoPersonagem(Enum):

        """
        EstadoPersonagem define o conjunto de estados possíveis da Personagem.

        É usado por ControloPersonagem para definir as transições e por MaquinaEstados para manter o estado actual.
        """

        PROCURA = 1
        INSPECCAO = 2
        OBSERVACAO = 3
        REGISTO = 4