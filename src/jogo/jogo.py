from ambiente.ambiente_jogo import AmbienteJogo
from ambiente.evento_jogo import EventoJogo
from personagem.personagem import Personagem

# 2 tipos de import Absolutos e Relativos
# Absolutos -> 
# Relativos -> comeca por "." é relativo ao modulo --- se estiver dentro do mesmo packege
class Jogo():
    """Classe Jogo representa o jogo, que é o ambiente onde o agente irá atuar. Esta classe é utilizada para representar o ambiente do jogo, onde o agente irá atuar, e para controlar o fluxo do jogo."""

    def __init__(self):
        self.__ambiente = AmbienteJogo()
        self.__personagem = Personagem(self.__ambiente) # Personagem requer uma instancia de Ambiente
        # Temos de instanciar o ambiente antes da personagem, porque o personagem precisa de uma referência ao ambiente para interagir com ele.
        self.__personagem.mostrar()

    def executar(self):
        while True:
            self.__ambiente.evoluir()
            self.__personagem.executar()
            self.__personagem.mostrar()
            if self.__ambiente.observar() == EventoJogo.TERMINAR:
                break

# Executar Jogo
if __name__ == "__main__":
    Jogo().executar()

    