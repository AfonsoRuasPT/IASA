from lib.agente.controlo import Controlo

'''
Na arquitectura de agente reactivo, o processamento interno que relaciona percepções com acções é modularizado num Controlo Reactivo.
'''

class ControloReact(Controlo): # herda de Controlo

    '''
    ControloReact implementa o controlo reactivo do agente.
    Realiza a interface Controlo delegando o processamento da percepção ao comportamento raiz da hierarquia comportamental.
    O resultado é a acção seleccionada pelo mecanismo de coordenação de comportamentos.

    ControloReact herda de Controlo.
    ControloReact tem uma associação com Comportamento.
    '''

    def __init__(self, comportamento): # recebe o comportamento
        self.__comportamento = comportamento 

    def processar(self, percepcao): 
        """
        Processar percepcao e retornar a accao associada ao comportamento.
        """
        return self.__comportamento.activar(percepcao) # activa o comportamento raiz com a percepção e devolve a acção seleccionada