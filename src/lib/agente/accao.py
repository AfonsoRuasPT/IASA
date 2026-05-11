from abc import ABC

'''
CONCEITO UML - INTERFACE e ESTEREÓTIPO «interface»
Em UML uma interface é um classificador que define um conjunto
coeso de características (operações) sem as implementar.
Define um contrato: qualquer classe que realize esta interface
compromete-se a implementar as suas operações.
No diagrama de classes do projecto, Accao aparece com a notação
de interface (círculo).
'''

class Accao(ABC):

    '''
    TEORIA - ACÇÃO no ciclo do Agente Inteligente
    A Acção representa o resultado do processamento do agente:
    aquilo que o agente executa sobre o ambiente depois de processar
    uma percepção. No modelo do agente inteligente,
    a Acção sai do módulo Actuar em direcção ao Ambiente.
    Esta interface garante que qualquer tipo de acção é tratado de forma homogénea
    pelo Agente, princípio do polimorfismo.


    ARQUITECTURA - relações desta classe
    Accao é uma interface de marcação: não declara métodos
    abstractos, serve apenas para tipificar objectos como "acções".
    AccaoJogo é a única realização desta interface neste projecto.
    '''

    """Interface que representa uma acção"""
    # PYTHON – ABC (Abstract Base Class)
    # ABC é a classe base do módulo "abc" (Abstract Base Classes).
    # Herdar de ABC torna esta classe abstracta em Python, impedindo
    # que seja instanciada directamente (Accao() daria erro).
    # É a forma Python de implementar o conceito UML de interface:
    # como Python não tem a palavra-chave "interface", usa-se ABC
    # com métodos @abstractmethod para forçar o contrato.
    # Aqui não há métodos abstractos declarados, funciona como
    # interface de marcação (marker interface), identificando
    # semanticamente que um objecto "é uma Acção".


'''
CONCEITO UML - REALIZAÇÃO
A relação de Realização em UML representa implementação:
uma classe realiza as características de uma interface.
AccaoJogo realiza Accao - herda dela e implementa o contrato.
No diagrama de classes usa-se uma seta tracejada com ponta
triangular vazia da classe para a interface.
'''
