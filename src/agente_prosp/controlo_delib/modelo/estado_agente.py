from mod.estado import Estado

class EstadoAgente(Estado):  # herda de Estado, 

    '''
    EstadoAgente representa a configuração do agente no espaço de estados, cada estado é definido pela posição (x, y) do agente no ambiente.
    O conjunto de todos os EstadoAgente possíveis forma o espaço de estados que o planeador explora para encontrar um percurso do estado inicial até ao estado objectivo.
 
    EstadoAgente herda de Estado.
    EstadoAgente tem uma associação com Posicao tuplo que indica a posição x e y do agente via atributo privado __posicao.
    '''

    def __init__(self, posicao):
        self.__posicao = posicao
        self.__id_valor = hash(posicao)
        """
        hash(self.__posicao) no metodo id_valor, no entanto dada a quantidado de estados que podem ser gerados, e a quantidade de
        vezes que iria ser chamado isso representaria um custo computacional elevado e desnecessario.

        Para dar a volta a esta situação calculamos o hash no atributo self.__id_valor no contrutor porque assim em vez de calcularmos o 
        hash cada ve que chamamos o metodo id_valor calculamos apenas uma vez o hash e "vamos apenas buscar" o valor ja calculado 
        associado ao objecto.
        """

    def id_valor(self):  # implementação do método abstracto de Estado
        return self.__id_valor # devolve o hash da posição usado para identificar o estado de forma única que foi calculado no construtor

    @property
    def posicao(self): # getter da posição
        return self.__posicao # devolve um tublo (x , y)