from agente.accao_jogo import AccaoJogo 
from ambiente.comando_jogo import ComandoJogo
from ambiente.evento_jogo import EventoJogo
from .estado_personagem import EstadoPersonagem
from agente.controlo import Controlo
from maqest.maquina_estados import MaquinaEstados 


class ControloPersonagem(Controlo):
    
    def __init__(self):
        procurar = AccaoJogo(ComandoJogo.PROCURAR)
        aproximar = AccaoJogo(ComandoJogo.APROXIMAR)
        observar = AccaoJogo(ComandoJogo.OBSERVAR)
        fotografar = AccaoJogo(ComandoJogo.FOROGRAFAR)
        self.__maq_est = MaquinaEstados(EstadoPersonagem.PROCURA, 
                                        [(EstadoPersonagem.PROCURA, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, aproximar),
                                         (EstadoPersonagem.PROCURA, EventoJogo.RUIDO, EstadoPersonagem.INSPECCAO, aproximar),
                                         (EstadoPersonagem.PROCURA, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA, procurar),

                                         (EstadoPersonagem.INSPECCAO, EventoJogo.RUIDO, EstadoPersonagem.INSPECCAO, procurar),
                                         (EstadoPersonagem.INSPECCAO, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, aproximar),
                                         (EstadoPersonagem.INSPECCAO, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA),

                                         (EstadoPersonagem.OBSERVACAO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, observar),
                                         (EstadoPersonagem.OBSERVACAO, EventoJogo.FUGA, EstadoPersonagem.INSPECCAO),

                                         (EstadoPersonagem.REGISTO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, fotografar),
                                         (EstadoPersonagem.REGISTO, EventoJogo.FUGA, EstadoPersonagem.PROCURA),
                                         (EstadoPersonagem.REGISTO, EventoJogo.FOTOGRAFIA, EstadoPersonagem.PROCURA)]) 
    
    def processar(self, percepcao):
        evento = percepcao.evento
        return self.__maq_est.processar(evento)
    
    @property
    def estado(self):
        return self.__maq_est.estado
    