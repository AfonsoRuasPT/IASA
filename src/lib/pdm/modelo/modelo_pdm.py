from abc import ABC, abstractmethod

class ModeloPDM(ABC):
    """
    Esta interface é responsavel por 
    """

    @abstractmethod
    def S(self):
        """Conjunto de Estados do Mundo"""
        # deve retornar uma lista de Estados

    @abstractmethod
    def A(self, s):
        """Conjunto de Acções Possíveis num Estado"""
        #deve retornar uma lista de Operadores


    @abstractmethod
    def T(self, s, a, sn):
        """Probabilidade de transição de "s" para "s'" atravez de "a" """
        #deve retornar um double

    @abstractmethod
    def R(self, s, a, sn):
        """Recompensa Esperada na Transição de "s" para "s'" através de "a" """
        #deve retornar um double

    @abstractmethod
    def suc(self, s, a):
        """Calculo dos estados sucessores"""
        # retorna a lista de estados sucessores calculados