from abc import abstractmethod

class Estado():

    """
    A classe Estado é a unidade de informação mais elementar do sistema, serve para representar uma única situação, momento ou 
    configuração do tabuleiro dentro da resolução do seu problema. O seu método id_valor tem a função de gerar e devolver uma 
    identificação única, assim como os metodos internos hash e eq que atribuem o id ao objeto e verifica a igualdade respetivamente. 
    
    Esta identificação é o que vai permitir ao mecanismo de procura comparar diferentes momentos e perceber de forma eficiente se 
    um determinado estado já foi explorado anteriormente, sendo vital para evitar que o algoritmo ande em círculos ou gaste memória
    desnecessária.
    """

    # retorna o hash, uma identificacao unica do estado
    def __hash__(self):
        return self.id_valor()
    
    # metodo equals em java, compara se os IDs´s dos estados sao iguais
    def __eq__(self, objeto):
        if isinstance(objeto, Estado):
            return self.__hash__() == objeto.__hash__()
        else:
            return False

    @abstractmethod
    def id_valor(self):
        """"""
