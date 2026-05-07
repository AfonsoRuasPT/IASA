from ecr.resposta import Resposta
from agente_prosp.accoes.rodar import Rodar

class RespostaEvitar(Resposta):
    """
    Resposta evitar para o comportamento evitar
    """

    def _obter_accao(self, percepcao):
        """
        Obter a accao de evitar um obstáculo.

        Esta accao é determinada pela direcção atual do agente.
        Rodamos o agente 90 graus para a direita.
        """
        dir_agente = percepcao.direccao # obter a direccao atual do agente
        dir_resposta = dir_agente.rodar() # agente roda no sentido dos ponteiros do relogio
        return Rodar(dir_resposta) # retorna a accao rodar