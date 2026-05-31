from .avaliador_heur import AvaliadorHeur
 
class AvaliadorSofrega(AvaliadorHeur): # herda de AvaliadorHeur
 
    '''
    AvaliadorSofrega implementa a Procura Sôfrega: f(n) = h(n).
    Ordena a fronteira apenas pela estimativa heurística do custo até ao objectivo,
    ignorando o custo já acumulado.
    '''
 
    """
    A classe AvaliadorSofrega é o cérebro que dita a regra da Procura Sófrega. 
    O seu método prioridade é extremamente direto: ele pega no estado do nó atual e devolve estritamente o valor que a 
    heurística calcula para ele (self.heuristica.h(no.estado)). 
    Em termos matemáticos, isto significa que f(n) = h(n). 
    Se a heurística diz que faltam "5 km", a prioridade é 5, ignorando por completo se o caminho para trás já custou muito ou 
    pouco custo/tempo.
    """
 
    def prioridade(self, no): # f(n) = h(n): prioridade é apenas a estimativa heurística do custo até ao objectivo
        return self.heuristica.h(no.estado)