from ecr.reaccao import Reaccao
from .resposta_evitar import RespostaEvitar
from .estimulo_obs import EstminuloObs

class EvitarObst(Reaccao):
    """
    Evitar obstaculo é issencioal para o bom funcionamento e para a continuidade do jogo por isso tera uma hirarquia media ficando
    no meio de AproximarAlvo e Explorar
    Este comportamento deve verificar a distancia que esta de cada obstaculo, se essa distancia for igual a 1 o agente deve rodar 90
    graus para a esquerda ou para a direita, com o conhecimento de que se ao rodar se depara com outro obstaculo deve rodar 
    para o mesmo lado
    """


    """
    Segundo a nossa arquitetura uma reaccao, é um modulo que associa um estimulo e uma resposta, 
    como estamos na class EvitarObst, o estumulo é o EstimuloObs, que é a class que deteta a distancia dos obstaculos,
    e a rtesposta é a RespostaEvitar, que é class que tem a accao de rodar o aguente para evitar o obstaculo.
    """
    def __init__(self):
        super().__init__(EstminuloObs, RespostaEvitar(None))