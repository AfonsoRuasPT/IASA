from .comportamento import Comportamento
from abc import abstractmethod

"""
O polimorfismo é um princípio fundamental que permite que 
objetos de diferentes classes sejam tratados como se fossem do mesmo tipo. 
Na prática, isto significa que podemos chamar o mesmo método em objetos diferentes, e cada um 
responderá de forma específica, de acordo com a sua própria implementação.

A relação entre estas classes baseia-se na herança, onde as classes "filhas" 
herdam da classe "mãe", e que podem redefenir ou não os seus metodos.
É exatamente esta relação hierárquica e de partilha de um "contrato" 
comum que torna o polimorfismo possível.

No nosso caso a classe ComportamentoComp é a classe mãe, e as classes Prioridade e Hierarquia são 
as classes filhas que são classes que vao implementar o metodo seleccionar_accao da classe mãe, ou seja 2 maneiras diferentes de fazer essa seleção
uma maneira hierarquica e uma maneira prioritaria.
"""

class ComportamentoComp(Comportamento):

    def __init__(self, comportamentos):

        """
        O comportamento composto é como o nome indica um conjunto de comportamentos, para selecionar um desses comportamentes para ser ativado existe uma seleccao se accao
        que é um metodo que temos tambem
        """
        self.__comportamentos = comportamentos # alterei isto

    def activar(self, percepcao): # retorna uma accao
        accoes = []
        for comportamento in self.__comportamentos: # para todos os comportamentos, activar o comportamento com base na percepção, que é uma accao
            accao = comportamento.activar(percepcao)
            if accao: # linha adicionada, nao estava
                accoes.append(accao) # se a accao for diferente de None, adicionar a accao à lista de accoes
        if accoes: # verificar se a lista tem accoes
            # print("ATIVAR")
            return self.seleccionar_accao(accoes) # selecionar a accao a partir do metodo seleccionar_accao
                # nao retornamos logo a accao porque esse criterio cabe ao metodo seleccionar_accao, respeitar a arquiterira, dependendo do critério podemos até nao retornar accao nenhuma, e caso queiramos alterar o criterio assim não temos de mexer neste método 
        
    @abstractmethod # metodo abstrato
    def seleccionar_accao(self, accoes): # retorna uma accao
        """"""