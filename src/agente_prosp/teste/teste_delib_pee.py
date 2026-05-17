from plan.plan_pee.planeador_pee import PlaneadorPEE
from agente_prosp.controlo_delib.controlo_delib import ControloDelib
from agente_prosp.agente_prosp import AgenteProsp
from sae import Simulador

if __name__ == "__main__":
    planeador = PlaneadorPEE()
    controlo = ControloDelib(planeador)
    agente = AgenteProsp(controlo)
    simulador = Simulador(1, agente, vista_modelo = True)
    simulador.executar()
