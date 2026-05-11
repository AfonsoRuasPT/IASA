from abc import abstractmethod, ABC

'''
CONCEITO UML - DIAGRAMA DE CLASSES (Perspectiva Estrutural)
Os diagramas de classes descrevem a organização estática de um
sistema: quais as partes que existem e como se relacionam entre si.
Cada classe corresponde directamente a uma "class" no diagrama
de classes UML do projecto.

CONCEITO UML - ABSTRACÇÃO E MODULARIZAÇÃO
A abstracção consiste em realçar o que é essencial
e omitir detalhes não relevantes. A classe Agente define o que
todo o agente deve saber fazer (percepcionar, actuar, executar)
sem dizer como o faz.
A modularização divide o sistema em partes coesas;
Agente é uma dessas partes, com responsabilidade clara.
'''

class Agente(ABC):

    '''
    TEORIA - AGENTE INTELIGENTE 
    Um Agente Inteligente é uma representação computacional de um
    sistema autónomo que opera no ciclo percepção→processamento→acção.
    Esta classe implementa esse ciclo: _percepcionar obtém
    informação do ambiente, _controlo.processar decide a acção, e
    _actuar executa-a. O agente é reactivo (responde a estímulos do
    ambiente) e autónomo (executa o ciclo sem intervenção externa).

    ARQUITECTURA - relação com Controlo, Percepcao, Accao
    Agente tem uma associação com Controlo:
    o controlo é criado fora e passado ao agente, acesso exclusivo
    via _controlo. Esta separação segue o princípio de encapsulamento:
    os detalhes de como se decide a acção ficam isolados
    em Controlo, e Agente apenas conhece a interface pública "processar".
    '''

    def __init__(self, controlo):
        # PYTHON – atributo protegido (convenção de um underscore "_")
        # Um único "_" antes do nome indica que o atributo é protegido:
        # por convenção só deve ser acedido dentro desta classe ou em
        # subclasses.
        self._controlo = controlo

    @abstractmethod
    def _percepcionar(self):
        """Obter percepção do ambiente. Retorna uma percepção"""
        # PYTHON – @abstractmethod (módulo abc)
        # Marca este método como abstracto: a classe Agente não o
        # implementa, obrigando qualquer subclasse concreta a fornecer
        # a sua própria implementação. Em UML corresponde a uma
        # operação abstracta numa classe abstracta (itálico no diagrama).
        # A docstring entre """ """ funciona como documentação do método
        # e tem o mesmo efeito sintáctico que "pass" mas é uma boa pratica
        # porque impede erro de bloco vazio.

    @abstractmethod
    def _actuar(self, accao):
        """Actua"""
        # PYTHON – segundo método abstracto
        # Cada agente concreto decide como actua sobre o

    def executar(self):
        # TEORIA – ciclo percepção-processamento-acção
        # O método executar implementa um passo completo do ciclo do
        # agente inteligente: percebe o ambiente, processa a percepção
        # para obter uma acção, e actua se a acção for válida.
        # Este ciclo é o núcleo de qualquer sistema autónomo reactivo.

        percepcao = self._percepcionar() # obtém percepção do ambiente chamando o método abstracto da subclasse

        accao = self._controlo.processar(percepcao) # delega a decisão ao Controlo, padrão de delegação: Agente utiliza Controlo processar, mantendo acoplamento baixo

        if accao is not None: # PYTHON – None é o valor que indica ausência de acção; usa-se "is not None" em vez de "!= None" porque é uma comparação de identidade (é o mesmo objecto None), não de valor
            return self._actuar(accao) # executa a acção concreta na subclasse
        return None # sem acção válida, o ciclo termina sem efeito

        """Executar acção no ambiente. Falta implementar o método executar da Classe Agente"""
        # raise NotImplementedError para dar erro caso o método seja chamado sem ser implementado


'''
CONCEITO UML - DIAGRAMA DE ACTIVIDADE
O método executar() é descrito por um diagrama de
actividade UML: nó inicial → percepcionar → processar → decisão
[accao is None / accao not None] → actuar → nó final.
Os diagramas de actividade representam o fluxo de controlo,
descrevendo sequências de acções e condições tal como
o "if accao is not None" no código.

CONCEITO UML - CLASSE ABSTRACTA vs INTERFACE
Agente é uma classe abstracta (tem métodos abstractos mas também
tem método concreto executar). Em UML o nome da classe abstracta
aparece em itálico. Percepcao, Accao e Controlo são interfaces
(só declaram comportamento, sem implementação) - em UML usam o
estereótipo «interface».
'''
