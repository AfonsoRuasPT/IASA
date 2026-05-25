from mod.problema import Problema

'''
Um Problema de Planeamento define os três elementos fundamentais:
  - Estado inicial: de onde o agente parte
  - Objectivo: o estado que se pretende atingir
  - Operadores: as acções que o agente pode realizar
O ProblemaPlan concretiza este conceito para o contexto do planeamento do agente.
'''

class ProblemaPlan(Problema): # herda de Problema, concretiza o problema de planeamento para a PEE

    '''
    ProblemaPlan define o problema de planeamento concreto para a PEE.
    Combina o ModeloPlan (estado inicial e operadores) com o estado final (objectivo) para formar o problema completo que o PlaneadorPEE
    passa ao mecanismo de procura.

    ProblemaPlan herda de Problema.
    ProblemaPlan tem uma associação com Estado.
    '''

    def __init__(self, modelo_plan, estado_final): # recebe o modelo de planeamento e o estado final
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        # invoca o construtor da super classe passando o estado inicial e os operadores extraídos do ModeloPlan
        # super().__init__ inicializa a super classe com os elementos necessários para a procura
        self.__estado_final = estado_final # EstadoAgente que representa o destino do plano

    def objectivo(self, estado): # verifica se um estado é o estado objectivo
        if estado == self.__estado_final: # compara o estado actual com o estado final
            return True
        else:
            return False
        # quando devolve True, a procura termina e o percurso encontrado é o plano