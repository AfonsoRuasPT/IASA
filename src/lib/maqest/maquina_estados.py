class MaquinaEstados():

    '''
    MaquinaEstados implementa o modelo formal de uma Máquina de Estados Finita de Mealy.
    É caracterizada por: λ : QxΣ → Z

    É uma Máquina de Mealy porque a saída λ depende do estado E do evento (slide 5 dinâmica).
    '''


    # transicoes -> [(EstadoAnt, Evento, EstadoSuc, Accao)]
    def __init__(self, estado_inicial, transicoes):
        self.__estado_inicial = estado_inicial
        self.__transicoes = transicoes
        self.__estado = estado_inicial
        self.__tte = {} # tabela transicao de estados
        self.__tae = {} # tabela accao de estados
        if transicoes:
            for transicao in transicoes:
                # comentar isto
                estado_ant, evento, estado_suc, accao = transicao \
                    if len(transicao) == 4 else transicao + (None, )
                self.definir_transicao(estado_ant, evento, estado_suc, accao)


    def definir_transicao(self, estado_ant, evento, estado_suc, accao = None):
        self.__tte[(estado_ant, evento)] = estado_suc
        if accao is not None: # "if accao" se for instancia -> True, se for None -> False, como accao pode ser uma instancia de qualquer coisa (enumerado, inteiro ect..) e se for 0 o codigo nunca vai avancar porque 0 converte para False
            self.__tae[(estado_ant, evento)] = accao

    def processar(self, evento):
        accao = self.__tae.get((self.__estado, evento)) # obter a acção correspondente ao estado atual e ao evento recebido, utilizando a tabela de acção de estados para mapear o par (estado, evento) para a acção correspondente
        novo_estado = self.__tte.get((self.__estado, evento)) # obter o novo estado correspondente ao estado atual e ao evento recebido, utilizando a tabela de transição de estados para mapear o par (estado, evento) para o novo estado correspondente
        if novo_estado is not None: # se o novo estado for diferente de None, ou seja, se houver uma transição de estado correspondente ao estado atual e ao evento recebido, None é uma marca de ausencia de valor, o != implica comparacao de valores ent aqui n dá, é um teste semantico
            self.__estado = novo_estado # atualizar o estado atual para o novo estado
        return accao # retornar a acção correspondente ao estado atual e ao evento recebido, que pode ser None se não houver uma acção correspondente ao estado atual e ao evento recebido

    @property
    def estado(self):
        return self.__estado
