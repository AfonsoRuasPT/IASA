from .mec_util import MecUtil

class PDM:

    '''
    Representação modular
    Calcula a politica e resolve o processo de decisao de markov.
    '''

    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__mec_util = MecUtil(self.__modelo, gama, delta_max)

    def politica (self, U): # A politica otima é para cada estado devemos escolher aquela com recompensa maior; em cada estado que accao deve ser feita?
        # qual a politica que maximiza a utilidade da accao
        S, A = self.__modelo.S, self.__modelo.A
        pol = {} # politica é um dicionarios que associa
        for s in S():
            if A(s): # se existirem accoes para este estado
                pol[s] = max(A(s), key=lambda a: self.__mec_util.util_accao(s, a, U)) 
                # funcao que recebe a accao e invoca o metodo util_accao
        return pol # retornamos apolitica

    def resolver(self): #
        U = self.__mec_util.utilidade()
        pol = self.politica(U)
        return U, pol
