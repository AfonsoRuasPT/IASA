from lib.mod.estado import Estado

class EstadoContagem(Estado):


    """
    Inunciado Problema Contagem:

    Dado um valor inicial, um valor fina le um conjunto de
    incrementos possiveis, que incrementos realizar para
    atingir ou superar o valor final.

    Para observar o efeito do custo na procura, o custo dos operadores corresponde ao quadrado do incremento.
    """

    """
    No ambito do nosso problema contagem o estado da contagem representa o valor atual da contagem.
    Utilizamos o valor da contagem como o identificador do estaado (id_valor) para garantir que cada estado é unicamente identificado.

    Neste nosso problema so existem operadores incrementais, se existicem operadores que decrimentassem a contagem nao invalidaria o 
    identificador ser o valor atual da contagem, uma vez que o mesmo valor do problema significa que o estado é o mesmo, 
    logo o id_valor retornaria o mesmo id para o estado com o mesmo valor de contagem, que é justamente o proposito do id_valor,
    identificar unicamente cada estado, se o estado for o mesmo retorna o mesmo valor.

    """

    def __init__(self, contagem):
        self.__contagem = contagem

    @property
    def contagem(self):
        return self.__contagem
    
    def id_valor(self): # implementacao do metodo abstrado id_valor que retorna o valor da contagem
        return self.__contagem