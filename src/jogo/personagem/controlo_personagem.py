from agente.accao_jogo import AccaoJogo 
from ambiente.comando_jogo import ComandoJogo
from ambiente.evento_jogo import EventoJogo
from .estado_personagem import EstadoPersonagem
from agente.controlo import Controlo
from maqest.maquina_estados import MaquinaEstados 


class ControloPersonagem(Controlo): # herda de Controlo, tem de implementar o método processar

    '''
    ControloPersonagem é a concretização de Controlo para a Personagem.
    Implementa a lógica de decisão da Personagem através da MaquinaEstados, definindo as transições de estado e acções correspondentes (slide 13 Parte1).

    ControloPersonagem compõe a MaquinaEstados no contrutor.
    Depende de AccaoJogo, ComandoJogo, EventoJogo e EstadoPersonagem para definir as transições.
    '''
    
    def __init__(self):
        # instanciar as acções de personagem possíveis
        procurar = AccaoJogo(ComandoJogo.PROCURAR)
        aproximar = AccaoJogo(ComandoJogo.APROXIMAR)
        observar = AccaoJogo(ComandoJogo.OBSERVAR)
        fotografar = AccaoJogo(ComandoJogo.FOROGRAFAR)

        # cada transição é um tuplo: (EstadoAnt, Evento, EstadoSuc, Accao)
        # ou (EstadoAnt, Evento, EstadoSuc) se não houver acção associada
        # as transições foram retiradas do diagrama de transição de estado da Personagem (slide 13 Parte1)
        self.__maq_est = MaquinaEstados(EstadoPersonagem.PROCURA,  # estado inicial
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
    
    def processar(self, percepcao): # implementação do método abstracto de Controlo, implementado com ajuda do diagrama de atividade (slide 15 Parte1)
        evento = percepcao.evento # extrai o EventoJogo da PercepcaoJogo
        return self.__maq_est.processar(evento) # a maquina de estados processa um evento e retorna uma accao
    
    @property
    def estado(self): # propriedade de leitura (read only)
        return self.__maq_est.estado # devolve o EstadoPersonagem actual