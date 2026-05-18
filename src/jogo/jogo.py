from ambiente.ambiente_jogo import AmbienteJogo
from ambiente.evento_jogo import EventoJogo
from personagem.personagem import Personagem
'''Esta class Jogo serve como main do nosso Parte1 do projeto, nestes casos não podemos usar imports relativos, somente imports absolutos'''



class Jogo():
    """Classe Jogo representa o jogo, que é o ambiente onde o agente irá atuar. Esta classe é utilizada para representar o ambiente do jogo, onde o agente irá atuar, e para controlar
      o fluxo do jogo."""
    
    '''
    Esta class instancia os objetos necessarios para o jogo e executa o jogo.
    '''

    def __init__(self):
        self.__ambiente = AmbienteJogo()
        self.__personagem = Personagem(self.__ambiente) # Personagem requer uma instancia de Ambiente
        # Temos de instanciar o ambiente antes da personagem, porque o personagem precisa de uma referência ao ambiente para interagir com ele.
        self.__personagem.mostrar()

    def executar(self):
        while True:
            self.__ambiente.evoluir() # evolui o ambiente
            self.__personagem.executar() # executa a personagem
            self.__personagem.mostrar() # mostra a personagem (prints)
            if self.__ambiente.observar() == EventoJogo.TERMINAR: # para o metodo com break se o eevento for TERMINAR
                break

# Executar Jogo
if __name__ == "__main__":
    Jogo().executar() # executamos o jogo

    