from .comportamento import Comportamento
from abc import abstractmethod

'''
O Comportamento Composto é um tipo de comportamento que agrega outros comportamentos (sub-comportamentos) e requer um mecanismo de selecção de acção para determinar
qual a acção a executar em função das respostas dos vários comportamentos internos.
Uma percepção pode potencialmente activar múltiplas reacções, gerando diferentes acções, pelo que é necessário seleccionar qual a acção a gerar à saída.
Os mecanismos de selecção disponíveis são:
  Hierarquia - os comportamentos têm prioridade fixa pela sua ordem na lista
  Prioridade - a acção com maior prioridade associada é seleccionada
'''

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

class ComportamentoComp(Comportamento): # herda de Comportamento; é também um comportamento mas composto por outros

    '''
    ComportamentoComp implementa o mecanismo base de um comportamento composto
    da biblioteca ECR. 
    Agrega uma lista de sub-comportamentos, activa todos perante uma percepção, recolhe as acções geradas e delega a selecção da acção final ao método abstracto seleccionar_accao,
    que é implementado pelas subclasses Hierarquia e Prioridade.

    ComportamentoComp herda de Comportamento.
    O simbolo 1*... no diagram da arquitetura significa que ComportamentoComp agrega um ou mais Comportamentos.
    '''

    def __init__(self, comportamentos): # recebe a lista de sub-comportamentos que este comportamento composto agrega
        """
        O comportamento composto é como o nome indica um conjunto de comportamentos, para selecionar um desses comportamentes para ser ativado existe uma seleccao se accao
        """
        self.__comportamentos = comportamentos # lista de Comportamentos, define os sub-comportamentos agregados

    def activar(self, percepcao): # activa todos os sub-comportamentos e selecciona a acção final
        accoes = []
        for comportamento in self.__comportamentos: # para todos os sub-comportamentos, activar com a percepção actual
            accao = comportamento.activar(percepcao)
            if accao: # só adiciona à lista se o comportamento foi activado 
                accoes.append(accao) # recolhe todas as acções geradas pelos sub-comportamentos activados
        if accoes: # se existir alguma accao na lista
            return self.seleccionar_accao(accoes) 
            # não retornamos logo a accao porque esse critério cabe ao método seleccionar_accao.

        
    @abstractmethod # metodo abstrato: cada subclasse define o seu mecanismo de selecção de acção
    def seleccionar_accao(self, accoes): # dada a lista de acções geradas, selecciona e devolve a acção final
        """"""