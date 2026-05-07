from random import random, choice
from ecr.comportamento import Comportamento
from sae import Direccao
from agente_prosp.accoes.rodar import Rodar
from agente_prosp.accoes.avancar import Avancar


class Explorar(Comportamento): # Explorar é um comportamento, por isso herda de Comportamento
    """
    O comportamento explorar sendo o mais "simples" penso que seja o comportamento mais em baixo na hierarquia, logo terá o indice 2
    Aleatoriamente anda e roda ah procura alvos
    """

    """
    Comprtamento explorar com movimentos em direções aletorias
    """

    def __init__(self, prob_rotacao = 0.7): # contrutor com atributo prob_rotacao que se oitido tem o valor default de 0.7
        self.__prob_rotacao = prob_rotacao  # defenir atributo privado prob_rotacao

    def activar(self, percepcao):           # activação do comportamento
                                            # nao usamos a "percepcao" porque explorar não depende de nenhum estimulo
        if random() < self.__prob_rotacao: # "random()" gera um numero entre 0 e 1
                                           # VERIFICAÇÃO - > verificamos de esse numero é menor que a probabilidade de rotacao

                                           # TRUE -> O agente roda para uma direcao aleatoria que pode ser NORTE SUL ESTE OESTE, do enumado DIRECCAO

            list_direccoes = list(Direccao) # "list(Direccao)" transforma o inumerado Direccao em uma lista
            dir_aleatoria = choice(list_direccoes) # "choice" escolhe um elemento da lista
            accao = Rodar(dir_aleatoria) # defenimos a accao
                                         
        else:                              # FALSE -> O agente avança

            accao = Avancar() # defenimos a accao
        return accao # retornamos a accao