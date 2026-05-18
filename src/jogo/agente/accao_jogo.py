from agente.accao import Accao

class AccaoJogo(Accao): # Herda de Accao que significa que é uma Accao concreta

    '''
    AccaoJogo é a representação concreta de uma acção. 

    '''

    def __init__(self, comando):
        self.__comando = comando # atributo privado (dois underscores "__") é inacessível fora da classe

    @property
    def comando(self):
        # @property é um getter, atributo de leitura
        # @property transforma este método num atributo de leitura (read only). 
        # Quem escreve accao.comando obtém o valor de __comando sem poder alterá-lo.
        # Em UML, a restrição {read only} nos diagramas do projecto corresponde exactamente a isto.
        # Segue o princípio de encapsulamento, o atributo privado fica protegido, e o acesso externo é exclusivamente através desta interface pública controlada.
        return self.__comando # devolve o comando encapsulado