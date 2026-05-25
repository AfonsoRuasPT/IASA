from abc import ABC, abstractmethod

'''
A Parte 2 introduz a arquitectura de agentes reactivos.
O comportamento é gerado de forma reactiva, com base em associações directas entre estímulos (derivados das percepções) e respostas (geradoras de acção).

A Biblioteca ECR Esquemas Comportamentais Reactivos organiza os elementos base desta arquitectura de forma modular:
  Comportamento - Interface que define a funcionalidade geral de um comportamento
  Reaccao       - Implementação do mecanismo base de uma reacção
  ComportComp   - Implementação do mecanismo base de um comportamento composto
  Estimulo      - Interface que define a funcionalidade geral de um estímulo
  Resposta      - Implementação do mecanismo base de uma resposta

Um comportamento é um conjunto de reacções relacionadas entre si no sentido de produzirem um resultado específico, por exemplo, evitar um obstáculo.
Relaciona padrões de percepção com padrões de acção e pode ter continuidade no tempo.
'''

class Comportamento(ABC): # interface base da biblioteca ECR

    '''
    Comportamento é a interface base da biblioteca ECR.
    Define o contrato mínimo de qualquer comportamento reactivo que é receber uma percepção e devolver uma acção. 

    Comportamento é realizado por Reaccao e ComportamentoComp.
    É usado por ControloReact (associação via atributo __comportamento).
    '''

    """
        Interface que activa a funcionalidade geral de um comportamento.  
     """

    @abstractmethod
    def activar(self, percepcao): # dado uma percepção, devolve a acção a executar 
        """Activar o comportamento com base na percepção. Falta implementar o método activar da Interface Comportamento"""


    """
    Interface/Módulo base que define a funcionalidade geral de um comportamento.
    
    Um comportamento é um módulo comportamental que relaciona padrões de perceção 
    com padrões de ação. Consiste num conjunto de reações relacionadas 
    entre si com o intuito de produzir um resultado específico (ex: evitar obstáculos).
    """