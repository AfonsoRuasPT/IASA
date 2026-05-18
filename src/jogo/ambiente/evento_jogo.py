from enum import Enum # importa a classe Enum do modulo enum para criar enumeracoes

class EventoJogo(Enum): # enumerado de eventos do jogo
    """
    EventoJogo define o conjunto de eventos possíveis no ambiente do jogo.

    É usado por AmbienteJogo para gerar eventos e por MaquinaEstados.
    """
    SILENCIO = "s"   
    RUIDO = "r"     
    ANIMAL = "a"    
    FUGA = "f"      
    FOTOGRAFIA = "o" 
    TERMINAR = "t"  

    def mostrar(self): # imprime o nome do evento actual
        print(f"\nEvento: {self.name}")