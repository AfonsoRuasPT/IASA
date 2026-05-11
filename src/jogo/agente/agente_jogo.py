from .percepcao_jogo import PercepcaoJogo
from agente.agente import Agente

'''
CONCEITO UML - GENERALIZAÇÃO / ESPECIALIZAÇÃO
AgenteJogo é uma especialização de Agente: herda toda a estrutura
e comportamento da classe base e acrescenta os detalhes específicos
do ambiente de jogo (como observar e executar via AmbienteJogo).
Em UML a relação de Generalização é a seta com ponta triangular
vazia da subclasse para a superclasse.
'''

class AgenteJogo(Agente):

    '''
    TEORIA - AGENTE concreto do Jogo
    AgenteJogo é a concretização do Agente Inteligente no contexto
    específico do jogo: sabe como percepcionar (observando o
    AmbienteJogo) e como actuar (executando um ComandoJogo no
    ambiente). Implementa os dois métodos abstractos de Agente,
    fechando o ciclo percepção-processamento-acção para este
    ambiente específico.

    ARQUITECTURA - relações desta classe
    AgenteJogo herda de Agente (generalização).
    AgenteJogo associa-se a AmbienteJogo via atributo privado
    __ambiente (associação unidirecional: o agente conhece o
    ambiente, mas o ambiente não conhece directamente o agente).
    AgenteJogo cria instâncias de PercepcaoJogo em _percepcionar,
    encapsulando o EventoJogo recebido, dependência de criação.
    A relação com Controlo é herdada de Agente (_controlo).
    '''

    def __init__(self, ambiente, controlo):
        super().__init__(controlo) # PYTHON – super().__init__: chama o construtor da super classe, classe pai
        # __init__(controlo) invoca o seu construtor para inicializar
        # o atributo protegido _controlo herdado. Sem esta chamada
        # _controlo não existiria e o método executar de Agente falharia.

        self.__ambiente = ambiente # atributo privado: AmbienteJogo; inacessível fora desta classe

    def _percepcionar(self):
        # TEORIA – Percepcionar: obter informação do ambiente
        # Implementação concreta do método abstracto de Agente.
        # Consulta o AmbienteJogo para obter o EventoJogo actual
        # e envolve-o numa PercepcaoJogo, que é o tipo concreto
        # de Percepcao neste projecto.
        evento = self.__ambiente.observar() # chama o método público observar do AmbienteJogo para obter o evento actual
        return PercepcaoJogo(evento) # cria e devolve uma PercepcaoJogo encapsulando o evento; PercepcaoJogo realiza a interface Percepcao

    def _actuar(self, accao):
        # TEORIA – Actuar: executar a acção no ambiente
        # Implementação concreta do método abstracto de Agente.
        # Extrai o ComandoJogo da AccaoJogo e passa-o ao AmbienteJogo.
        # O ambiente trata de mostrar/executar o comando.
        self.__ambiente.executar(accao.comando) # acede ao ComandoJogo via propriedade pública "comando" de AccaoJogo e executa-o no ambiente


'''
CONCEITO UML - POLIMORFISMO
Agente declara _percepcionar e _actuar como abstractos.
AgenteJogo fornece implementações concretas.
Quando o método executar de Agente chama self._percepcionar(),
o Python usa despacho dinâmico (polimorfismo) para chamar a
versão correcta conforme o tipo real do objecto em execução.
Isto permite que o método executar funcione de forma homogénea
independentemente de qual agente concreto está a ser executado.

CONCEITO UML - IMPORT ABSOLUTO vs RELATIVO
"from .percepcao_jogo import PercepcaoJogo" - import relativo:
  O "." refere-se ao package actual (mesmo directório).
  Usa-se dentro do mesmo package para referências internas.

"from agente.agente import Agente" - import absoluto:
  Especifica o caminho completo a partir da raiz do projecto.
  Usa-se para referências entre packages diferentes.
'''
