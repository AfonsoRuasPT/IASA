from ecr.prioridade import Prioridade
from sae import Direccao
from .aproximar_dir import AproximarDir

class AproximarAlvo(Prioridade):
    """
    Aproximar o alvo, sendo o objetivo do jogo é o comportamento mais importante logo tera a primeira posicao na lista
    Verifica a sua "visao" e anda na direcao do alvo, rodando e andando na sua direcao
    """

    """
    permite aproximar alvos em multiplas direcoes

    com base em comportamentos mais simples que é direcional cada um é uma reacao associadoa a uma direcao NORTE, SUL, ESTE, OESTE
    uma instancia de aproximar alvo é uma direcao selecionada atravez de prioridade
    A funcao "detectar" detecta a intencidade do estimulo que é um float

    a gama é uma parametro que vai ter utilizado para calcular a prioridade
    """

    """
    Permite que o agente se aproxime de um alvo avaliando múltiplas direções em simultâneo.
    Esta classe atua como um seletor herda de prioridade, que tambem significa que é um comportamento composto.
    
    Tem 4 comportamentos direcionais, associados aos eixos 
    NORTE, SUL, ESTE e OESTE.
       
    Cada direção consulta um 'EstimuloAlvo' correspondente. Este estímulo utiliza o
    método para calcular um valor que representa o quão favorável é mover para essa direção esse valor é o gama que calcula a prioridade de cada direcao.
    
    A classe AproximarAlvo compara as prioridades (estímulos) das 4 direções, seleciona a direção com o valor 
    mais alto.
    """

    def __init__(self):
        """
                super().__init__([AproximarDir(Direccao.NORTE), 
                          AproximarDir(Direccao.SUL), 
                          AproximarDir(Direccao.ESTE), 
                          AproximarDir(Direccao.OESTE)])
        """
                            # mesma coisa que o comentario em cima
        """
        Sendo o Aproximar alvo um comportamento composto, ele é composto por 4 comportamentos mais simples, que são os AproximarDir,
        cada um associado a uma direcao, e cada um desses comportamentos tem um estimulo associado a essa direcao, o EstimuloAlvo, 
        que calcula a prioridade de cada direcao, e o comportamento composto seleciona a direcao com a maior prioridade.
        Por isso passamos uma lista com os 4 comportamentos numa lista.
        """
        super().__init__([AproximarDir(direccao) for direccao in Direccao]) # utiliza os geradodes do python, lista por intenção.



    