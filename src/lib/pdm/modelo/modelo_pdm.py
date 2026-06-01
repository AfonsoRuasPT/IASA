from abc import ABC, abstractmethod

"""
Para que o mecanismo PDM possa funcionar com qualquer representação do mundo, é necessário definir um contrato comum, essa é a função de ModeloPDM.

Um Processo de Decisão de Markov é definido formalmente pelo tuplo
S, A, T, R:
  S         — conjunto de estados do mundo
  A(s)      — conjunto de acções possíveis no estado s
  T(s,a,s') — probabilidade de transição de s para s' através de a
  R(s,a,s') — recompensa esperada na transição de s para s' através de a
"""

"""
Define os cinco métodos que qualquer modelo PDM deve fornecer ao mecanismo
de resolução, o conjunto de estados S, o conjunto de acções
A(s), o modelo de transição T(s,a,s'), o modelo de recompensa R(s,a,s') e
a função de estados sucessores suc(s,a).
"""

class ModeloPDM(ABC):
    """
    ModeloPDM define o contrato mínimo que qualquer modelo PDM deve cumprir.
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