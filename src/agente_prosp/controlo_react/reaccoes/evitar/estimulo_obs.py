from ecr.estimulo import Estimulo

class EstminuloObs(Estimulo):

    INTENS_OBS = 1 # atributo estatico da class EstimulosObs
    # self.INTENS_OBS para obter o valor do atributo estatico da classe
    # EstminuloObs.INTENS_OBS = ... para definir o valor do atributo estatico da classe

    def detectar(percepcao):
        """
        Detetar a intensidade do estímulo de um obstáculo.
        """
        # utilizar operdor ternario para no detetar retornar 0 se n tiver um obstaculo presente e devolver 1
        
        # retonamos INTENS_OBS se o agente detetar um obstaculo, caso contrario retirnamos 0
        return EstminuloObs.INTENS_OBS if percepcao.contacto_obst() else 0 # retorna 1 se o elemento for um ALVO ou 0 se não for