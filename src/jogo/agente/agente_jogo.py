from .percepcao_jogo import PercepcaoJogo
from agente.agente import Agente

'''
"from .percepcao_jogo import PercepcaoJogo" - import relativo:
  O "." refere-se ao package actual (mesmo directório). Usa-se dentro do mesmo package para referências internas.

"from agente.agente import Agente" - import absoluto:
  Especifica o caminho completo a partir da raiz do projecto. Usa-se para referências entre packages diferentes.
'''

class AgenteJogo(Agente): # herda de agente, tem de implementar os metodos _percepcionar e _actuar

    '''
    AgenteJogo é a concretização do Agente no contexto do jogo.
    Implementa os dois métodos abstractos de Agente.


    AgenteJogo tem uma associação com AmbienteJogo.
    AgenteJogo cria uma instância de PercepcaoJogo em _percepcionar, encapsulando o EventoJogo recebido.
    Herdada de Agente.
    '''

    def __init__(self, ambiente, controlo): # recebe ambiente e controlo como parametros
        super().__init__(controlo) # super().__init__(controlo) invoca o seu construtor da super class para inicializar o atributo protegido _controlo herdado. 
        self.__ambiente = ambiente # atributo privado: AmbienteJogo; inacessível fora desta classe

    def _percepcionar(self): # obter informação do ambiente
                             # Implementação concreta do método abstracto de Agente.
        evento = self.__ambiente.observar() # chama o método público observar do AmbienteJogo para obter o evento actual
        return PercepcaoJogo(evento) # cria e devolve uma PercepcaoJogo encapsulando o evento

    def _actuar(self, accao): # executar a acção no ambiente
                              # Implementação concreta do método abstracto de Agente.
        self.__ambiente.executar(accao.comando) # acede ao ComandoJogo via propriedade pública "comando" de AccaoJogo e executa-o no ambiente


