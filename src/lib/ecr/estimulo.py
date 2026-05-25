from abc import ABC, abstractmethod

'''
O Estímulo é o elemento da reacção responsável por detectar a presença e intensidade de uma condição relevante na percepção.
'''

class Estimulo(ABC): # interface da biblioteca ECR; define o contrato de qualquer estímulo

    '''
    Estimulo é a interface da biblioteca ECR que define o contrato de detecção de estímulos. Cada subclasse concreta implementa detectar() de acordo com o tipo
    de estímulo a detectar.
    Devolve um float que representa a intensidade do estímulo: 0 se não detectado,
    valor > 0 proporcional à relevância do estímulo.

    Estimulo é realizado por EstimuloAlvo e EstimuloObs.
    '''

    # Define informação activadora de uma reacção

    @abstractmethod
    def detectar(self, percepcao): # dado uma percepção, devolve a intensidade do estímulo (float); 0 se não detectado
        """"""