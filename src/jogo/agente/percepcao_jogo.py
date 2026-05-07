from agente.percepcao import Percepcao

class PercepcaoJogo(Percepcao):

    def __init__(self, evento):
        self.__evento = evento

    @property
    def evento(self):
        return self.__evento