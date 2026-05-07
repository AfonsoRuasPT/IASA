from enum import Enum # impor da classe Enum do modulo enum para criar enumeracoes

class EventoJogo(Enum):
    """Enumeração dos eventos do jogo"""
    SILENCIO = "s"
    RUIDO = "r"
    ANIMAL = "a"
    FUGA = "f"
    FOTOGRAFIA = "o"
    TERMINAR = "t"

    def mostrar(self):
        print(f"\nEvento: {self.name}") 