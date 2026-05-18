from enum import Enum # impor da classe Enum do modulo enum para criar enumeracoes

class ComandoJogo(Enum):
    """
    Classe ComandoJogo representa um comando do jogo, que pode ser utilizado para controlar o ambiente do jogo. 
    Esta classe é utilizada para representar os comandos que o agente pode executar no ambiente do jogo.
    """
    PROCURAR = 1
    APROXIMAR = 2
    OBSERVAR = 3
    FOROGRAFAR = 4

    def mostrar(self): 
        print(f"\nAcção: {self.name}") 
        """imprimir o comando do jogo, utilizando o valor do comando do jogo para identificar o comando, 
        o value é um atributo da classe Enum que retorna o valor do elemento do enumerado, ou seja, o 
        valor associado ao comando do jogo, que é definido na declaração da classe ComandoJogo, por exemplo, 
        PROCURAR tem o valor 1, APROXIMAR tem o valor 2, OBSERVAR tem o valor 3 e FOROGRAFAR tem o valor 4"""