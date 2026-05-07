from lib.agente.agente import Agente
import sae

class AgenteProsp(Agente):

    def _percepcionar(self):
        return sae.transdutor.percepcionar()

    def _actuar(self, accao):
        return sae.transdutor.actuar(accao)
