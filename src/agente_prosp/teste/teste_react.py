from agente_prosp.controlo_react.reaccoes.recolher.recolher import Recolher
from agente_prosp.controlo_react.reaccoes.explorar.explorar import Explorar
from agente_prosp.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente_prosp.controlo_react.reaccoes.explorar.explorar_mem import ExplorarMem
from agente_prosp.controlo_react.controlo_react import ControloReact
from agente_prosp.agente_prosp import AgenteProsp
from sae import Simulador

# criar uma instancia de agente prosp que internamente tem um controlo reactivo com um comportamento de instancia explorar

"""
AgenteProsp não tem construtor, mas herda de Agente que recebe como parametro um controlo, ControloReact é um controlo.
O controlo tem como parametros um comportamento, e Ecplorar é um comportamento.
"""


if __name__ == "__main__":

    comportamento = Recolher() # intanciar o comportamento Explorar
    controlo = ControloReact(comportamento) # intanciar o controlo ControloReact com o comportamento
    agente = AgenteProsp(controlo) # instanciar o agente AgenteProsp com o controlo
    simulador = Simulador(1, agente)
    simulador.executar()


    """
    O agente, quando encarado com uma parede e tenta andar para a frente o agente fica vermelho, que significa a colidir com o obstaculo.
    O agente colide com o obstaculo porque ainda nao está implementado o evitar obstaculos, o comportamento explorar, o unico implementado até agora,
    apenas tem a capacidade de andar e rodar, mas nao tem a capacidade de evitar obstaculos, por isso o agente colide com a parede, ficando vermelho.
    Uma vez que evitar obstaculo no nosso comportamento composto, recolher,  com os comprtamentos AproximarAlvo, EvitarObstaculo e Explorar,
    nesta ordem de hierarquia significa que uma vez o comportamento EvitarObstaculos seja implementado, evita obstaculos, e só depois explora,
    logo o agente nunca mais irá colidir com a parede.

    Para implementar o comportamento evitar obstaculos teremos de verificar se a frente do agente esta um obstaculo e se esse obstaculo esta 
    a uma distancia de 1 bloco,se isto acontecer o agente tera de rodar até que já nao se encontra a distancia de 1 bloco um obstaculo.
    """
