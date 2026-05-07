from mod.estado import Estado
from mod.operador import Operador

class PassoSolucao(): # PassoSolucao nao herda nem Estado nem Solucao


    """
    A classe PassoSolucao guarda o estado atual e a ação (o operador) associada.
    Quando criamos um passo passamos-lhe o estado e o operador, e a classe guarda-os. 
    Como no código só usamos o @property (read only), garantimos que esses dados ficam imutáveis. 
    Ou seja, o código não permite a alteração dessa informação durante a execução.
    O objetivo desta classe é guardar todos os passos que constituem a solução final do problema, contendo o estado e o operador 
    utilizado. 
    """

    def __init__(self, estado, operador):
        self.__estado = estado
        self.__operador = operador

    @property #objeto imutavel, nao pode ser alterado depois de criado
    def estado(self):
        return self.__estado
    
    @property #objeto imutavel, nao pode ser alterado depois de criado
    def operador(self):
        return self.__operador

    