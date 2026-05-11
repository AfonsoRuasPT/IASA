from abc import ABC, abstractmethod

'''
CONCEITO UML - INTERFACE «interface» Controlo
Controlo é uma interface UML: define o contrato "processar uma
percepção e devolver uma acção" sem ditar como isso é feito.
No diagrama de classes do projecto Controlo aparece com notação de interface (círculo
ou «interface») associada à classe Agente por composição.
'''

class Controlo(ABC):

    '''
    TEORIA - Módulo de Processamento do Agente
    No modelo do agente inteligente, o módulo Controlo corresponde
    ao bloco "Processar": recebe a percepção do ambiente e decide
    qual a acção a executar. É aqui que reside a inteligência do
    agente, a lógica de decisão (reactiva, deliberativa ou híbrida).

    ARQUITECTURA - relação com Agente e ControloPersonagem
    Agente tem uma associação com Controlo (atributo _controlo).
    Esta ligação é acoplamento: Agente só conhece a
    interface Controlo, não sabe que existe ControloPersonagem.
    Isto segue o princípio de encapsulamento: os
    detalhes internos de ControloPersonagem ficam ocultos,
    e o Agente acede exclusivamente via "processar".
    '''

    @abstractmethod
    def processar(self, percepcao):
        """Processar a percepção e retornar uma acção. Falta implementar o método processar da Interface Controlo"""
        # PYTHON – @abstractmethod em interface ABC
        # Como Controlo é uma interface (ABC sem implementação),
        # "processar" é declarado abstracto para obrigar todas as
        # subclasses concretas a fornecer
        # a sua implementação específica.
        # A assinatura processar(self, percepcao) define o
        # contrato: recebe uma Percepcao, devolve uma Accao (ou None).


'''
CONCEITO UML - DIAGRAMA DE SEQUÊNCIA 
A interacção entre Agente e Controlo pode ser descrita num
diagrama de sequência: o objecto agente envia a mensagem
processar(percepcao) ao objecto controlo e recebe accao
como valor de retorno. No diagrama do projecto vê-se exactamente esta
sequência: Personagem → ControloPersonagem → MaquinaEstados.

CONCEITO PYTHON - self
Em Python, "self" é o primeiro parâmetro de qualquer método de
instância e refere-se ao próprio objecto. Quando se escreve
self._controlo, acede-se ao atributo _controlo desse
objecto específico.
'''
