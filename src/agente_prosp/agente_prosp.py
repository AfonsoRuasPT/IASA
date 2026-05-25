from lib.agente.agente import Agente
import sae
 
'''
O AgenteProsp é a concretização do Agente Inteligente para o problema de prospecção que "navega" por um espaço com obstáculos, desviando-se dos obstáculos
e recolhendo alvos. 
Opera com arquitectura reactiva que percebe o ambiente via transdutor e actua via transdutor.
'''
 
class AgenteProsp(Agente): # herda de Agente
 
    '''
    AgenteProsp é a concretização do Agente para o ambiente de prospecção.
    Implementa os dois métodos abstractos de Agente usando o transdutor SAE, que faz a interface entre o agente e o ambiente físico/virtual.
 
    AgenteProsp herda de Agente.
    AgenteProsp tem uma dependência com sae.transdutor.
    '''
 
    def _percepcionar(self): # obtém a percepção do ambiente via transdutor SAE
        return sae.transdutor.percepcionar() # delega ao transdutor que faz a interface com o ambiente e devolve uma Percepcao
 
    def _actuar(self, accao): # executa a acção no ambiente via transdutor SAE
        return sae.transdutor.actuar(accao) # delega ao transdutor que converte a Accao num movimento físico no ambiente