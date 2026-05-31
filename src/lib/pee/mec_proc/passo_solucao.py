from mod.estado import Estado
from mod.operador import Operador
 
class PassoSolucao():
 
    '''
    PassoSolucao é a unidade de informação de cada passo da solução. Guarda o estado em que o agente se encontrava e o operador executado nesse estado para avançar para 
    o passo seguinte.
    É imutável: após criado, estado e operador não podem ser alterados garantindo a integridade do percurso solução.
 
    PassoSolucao tem uma associação com Estado e com Operador.
    É criado por Solucao.
    '''
 
    """
    A classe PassoSolucao guarda o estado atual e a ação (o operador) associada.
    Quando criamos um passo passamos-lhe o estado e o operador, e a classe guarda-os. 
    Como no código só usamos o @property (read only), garantimos que esses dados ficam imutáveis. 
    Ou seja, o código não permite a alteração dessa informação durante a execução.
    O objetivo desta classe é guardar todos os passos que constituem a solução final do problema, contendo o estado e o operador 
    utilizado. 
    """
 
    def __init__(self, estado, operador): # recebe o estado e o operador que formam este passo da solução
        self.__estado = estado # Estado em que o agente se encontra neste passo
        self.__operador = operador # Operador executado para avançar para o próximo estado
 
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador