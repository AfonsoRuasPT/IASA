from agente.accao import Accao

class AccaoJogo(Accao):
    """Classe AccaoJogo representa uma ação do jogo."""
    
    def __init__(self, comando):
        self.__comando = comando 

    @property
    def comando(self): # read only
        return self.__comando