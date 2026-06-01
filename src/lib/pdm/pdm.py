from .mec_util import MecUtil

class PDM:

    """
    O PDM coordena o processo completo de resolução que calcula primeiro a função de utilidade U(s) através do MecUtil, e depois calcula a política óptima π*(s)
    a partir dessa utilidade.

    Política óptima:
    π*(s) = argmax_a Σ_{s'} T(s,a,s') * [R(s,a,s') + Y * U(s')]

    Para cada estado s, a política óptima escolhe a acção a que maximiza a utilidade esperada, é uma política determinista:
    π: S -> A(s), para cada estado indica uma acção específica a realizar.

    A separação entre MecUtil (calcula U) e PDM (deriva π e coordena) segue o princípio de responsabilidade única, ou seja, cada classe tem uma função clara e bem delimitada.
    """


    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__mec_util = MecUtil(self.__modelo, gama, delta_max)

    def politica (self, U): # A politica otima é para cada estado devemos escolher aquela com recompensa maior; em cada estado que accao deve ser feita?
        # qual a politica que maximiza a utilidade da accao

        """
        Para cada estado s com acções disponíveis, selecciona a acção a que
        maximiza util_accao(s, a, U) —que é acção com maior utilidade esperada.
        Devolve um dicionário EstadoAgente -> OperadorMover.
        """
        S, A = self.__modelo.S, self.__modelo.A
        pol = {} # politica é um dicionarios que associa
        for s in S():
            if A(s): # se existirem accoes para este estado
                pol[s] = max(A(s), key=lambda a: self.__mec_util.util_accao(s, a, U)) 
                # funcao que recebe a accao e invoca o metodo util_accao
                # max() com key: selecciona o elemento de A(s) que maximiza o valor devolvido pela função key.
                # lambda define uma função que recebe a acção a e devolve a sua utilidade.
                #  para cada a em A(s), calcular util_accao(s,a,U), e guardar o a com o maior valor.
        return pol # retornamos a politica

    def resolver(self): #
        U = self.__mec_util.utilidade() # calcula a função de utilidade
        pol = self.politica(U) # calcula a política óptima
        return U, pol # retorna a utilidade e a politica
