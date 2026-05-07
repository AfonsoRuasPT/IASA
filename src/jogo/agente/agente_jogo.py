from .percepcao_jogo import PercepcaoJogo
from agente.agente import Agente

class AgenteJogo(Agente):
    
    def __init__(self, ambiente, controlo):
        super().__init__(controlo) # chamar o construtor da classe pai Agente para inicializar o atributo protegido controlo com o valor do argumento controlo
        self.__ambiente = ambiente # inicializar o atributo privado ambiente com o valor do argumento ambiente, que é o ambiente do jogo onde o agente irá atuar

    def _percepcionar(self):
        evento = self.__ambiente.observar() # obter a percepção do ambiente do jogo utilizando o método observar do ambiente do jogo, que é um método público para obter a percepção do ambiente do jogo, e guardar a percepção obtida na variável var
        return PercepcaoJogo(evento)
        

    def _actuar(self, accao):
        self.__ambiente.executar(accao.comando) # executar a acção no ambiente do jogo utilizando o método executar do ambiente do jogo