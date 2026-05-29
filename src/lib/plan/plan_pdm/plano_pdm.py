from plan.plano import Plano

class PlanoPDM(Plano):

    '''
    Comentar relacao com Plano PEE
    Basicamente sao implementacao polimorficas da mesma interface, implementao os mesmos metodos mas com base em tipos de 
    raciocinio automatico diferente.
    '''

    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        if self.__politica:
            return self.__politica.get(estado)

    def mostrar(self, vista):
        for estado, valor in self.__utilidade.items():
            vista.mostrar_valor_posicao(estado.posicao, valor)
        for estado, accao in self.__politica.items():
            vista.mostrar_vector(estado.posicao, accao.ang)
