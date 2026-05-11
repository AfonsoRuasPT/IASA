from agente.accao import Accao

'''
CONCEITO UML - REALIZAÇÃO
AccaoJogo realiza a interface Accao: herda dela e concretiza o
contrato "ser uma acção". No diagrama de classes do projecto vê-se a relação
de realização AccaoJogo → Accao e a associação com ComandoJogo.
'''

class AccaoJogo(Accao):

    '''
    TEORIA - ACÇÃO concreta do Agente no Jogo
    AccaoJogo é a representação concreta de uma acção que a
    Personagem executa no AmbienteJogo. Encapsula um ComandoJogo
    e expõe-no de forma controlada.
    Corresponde ao "Actuar" do ciclo percepção-processamento-acção:
    depois de ControloPersonagem decidir a acção, cria uma
    AccaoJogo com o ComandoJogo adequado, e AgenteJogo extrai
    o comando para passar ao ambiente.

    ARQUITECTURA - relações desta classe
    AccaoJogo associa-se a ComandoJogo: tem um atributo privado
    __comando do tipo ComandoJogo. Esta é uma associação
    unidirecional (AccaoJogo conhece ComandoJogo, não o inverso).
    AccaoJogo realiza Accao (herança de interface).
    '''

    def __init__(self, comando):
        self.__comando = comando # PYTHON – atributo privado (dois underscores "__"):
        # atributo inacessível fora da classe
        # Em UML isto corresponde à visibilidade privada.

    @property
    def comando(self):
        # PYTHON – @property: getter = atributo de leitura
        # @property transforma este método num atributo
        # de leitura (read only). Quem escreve accao.comando obtém
        # o valor de __comando sem poder alterá-lo.
        # Em UML, a restrição {read only} nos diagramas do projecto
        # corresponde exactamente a isto.
        # Segue o princípio de encapsulamento: o atributo
        # privado fica protegido, e o acesso externo é exclusivamente
        # através desta interface pública controlada.
        return self.__comando # devolve o ComandoJogo encapsulado


'''
CONCEITO UML - ATRIBUTOS E VISIBILIDADE
No diagrama de classes UML, a visibilidade dos atributos é indicada
por símbolos:  + público,  - privado,  # protegido.

  sem underscore  → público    (acessível em qualquer lugar)
  _underscore     → protegido  (apenas na classe e subclasses)
  __underscore    → privado    (apenas dentro da própria classe)
'''
