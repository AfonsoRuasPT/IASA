from plan.plano import Plano

class PlanoPDM(Plano):

    '''
    Comentar relacao com Plano PEE
    Basicamente sao implementacao polimorficas da mesma interface, implementao os mesmos metodos mas com base em tipos de 
    raciocinio automatico diferente.
    '''

    """
O PlanoPDM  encapsula uma politica, um dicionário que mapeia cada estado para a acção
óptima a realizar nesse estado.

Política determinista π*(s) -> a: para cada estado s, indica uma acção
específica a realizar — a que maximiza a utilidade esperada.

A utilidade U(s) reflecte o valor a longo prazo de cada estado, é a soma
das recompensas descontadas esperadas ao longo de uma sequência de estados.
    """

    def __init__(self, utilidade, politica):
        """
        Herda de Plano
        """

        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        # Devolve o operador óptimo para o estado actual do agente, atravez da política calculada pelo PDM.
        if self.__politica:
            return self.__politica.get(estado)

    def mostrar(self, vista): # renderiza o plano na vista gráfica
        for estado, valor in self.__utilidade.items():
            vista.mostrar_valor_posicao(estado.posicao, valor)
        for estado, accao in self.__politica.items():
            vista.mostrar_vector(estado.posicao, accao.ang)
