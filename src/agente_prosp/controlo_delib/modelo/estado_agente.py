from mod.estado import Estado

class EstadoAgente(Estado):

    '''
    Especializa o Estado
    '''

    def __init__(self, posicao):
        self.__posicao = posicao
        self.__id_valor = hash(posicao)
        """
        hash(self.__posicao) no metodo id_valor, no entanto dada a quantidado de estados que podem ser gerados, e a quantidade de
        vezes que iria ser chamado isso representaria um custo computacional elevado e desnecessario.

        Para dar a volta a situaca calculamos o hash no atributo self.__id_valor no contrutor porque assim em vez de calcularmos o 
        hash cada ve que chamamos o metodo id_valor calcolamos apenas uma vez o hash e "vamos apenas buscar" o valor ja calculado 
        associado ao objecto.
        """

    def id_valor(self):
        return self.__id_valor

    @property
    def posicao(self):
        return self.__posicao