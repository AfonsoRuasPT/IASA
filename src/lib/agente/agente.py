from abc import ABC, abstractmethod

class Agente(ABC):

    def __init__(self, controlo):
        self._controlo = controlo # um "_" significa que é um atributo protefctedo, ou seja, só pode ser acedido dentro da classe ou por classes filhas

    @abstractmethod
    def _percepcionar(self):
        """Obter percepção do ambiente. Retorna uma percepção""" # Doc string, instrucao sintatica informativa que tem o mesmo efeito qure o pass

    @abstractmethod
    def _actuar(self, accao):
        """Actua"""

    def executar(self):
        percepcao = self._percepcionar() # obter percepção do ambiente
        accao = self._controlo.processar(percepcao) # processar a percepção para obter a acção a executar
        if accao is not None: # se a acção for diferente de None, ou seja, se houver uma acção a executar, None é uma marca de ausencia de valor, o != implica comparacao de valores ent aqui n dá, é um teste semantico
            return self._actuar(accao) # executar a acção
        return None # se não houver acção a executar, retorna None

        """Executar acção no ambiente. Falta implementar o método executar da Classe Agente"""
        # raise NotImplementedError para dar erro caso o método seja chamado sem ser implementado