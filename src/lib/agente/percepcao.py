from abc import ABC, abstractmethod

'''
CONCEITO UML - INTERFACE «interface» Percepcao
Percepcao é uma interface de marcação: define o tipo "percepção"
sem impor operações concretas. No diagrama de classes do projecto
aparece associada ao Agente e realizada por PercepcaoJogo.
'''

class Percepcao(ABC):

    '''
    TEORIA - PERCEPÇÃO no ciclo do Agente Inteligente
    A Percepção é a informação que o agente recolhe do ambiente
    através dos seus sensores (ou, no caso virtual, através do
    método observar do AmbienteJogo). No modelo do agente , a Percepção entra no módulo Percepcionar e é depois
    passada ao módulo Processar (Controlo).
    Esta interface garante que Agente e Controlo lidam com qualquer
    tipo de percepção de forma homogénea, sem depender de detalhes
    concretos como "é um EventoJogo" - princípio da abstracção:
    realça o essencial (é uma percepção) e omite
    detalhes (qual o tipo de dado específico que transporta).

    ARQUITECTURA - relação com AgenteJogo e PercepcaoJogo
    Percepcao não tem relações directas com outras classes nesta
    interface: é ponto de entrada do contrato. AgenteJogo cria
    instâncias de PercepcaoJogo (que realiza Percepcao) e passa-as
    a Controlo.processar. O acoplamento é fraco: Controlo recebe
    uma Percepcao.
    '''

    """Interface que representa uma percepção"""
    # PYTHON – ABC como interface de marcação
    # Tal como Accao, Percepcao herda de ABC mas não declara métodos
    # abstractos. Serve como "etiqueta de tipo": qualquer classe que
    # herdar de Percepcao fica identificada como sendo uma percepção,
    # permitindo verificações de tipo coerentes.


'''
CONCEITO UML - PERSPECTIVA ESTRUTURAL vs COMPORTAMENTAL
As interfaces Accao, Controlo e Percepcao pertencem à perspectiva
estrutural do modelo UML (definem as partes do sistema e as suas
relações). O comportamento dinâmico (transições) 
é capturado pelos diagramas de transição de estado
e de actividade, implementados na MaquinaEstados e no método
executar de Agente.

CONCEITO UML - GENERALIZAÇÃO / REALIZAÇÃO
Percepcao (interface) <- realizada por <- PercepcaoJogo (classe)
Accao     (interface) <- realizada por <- AccaoJogo     (classe)
Controlo  (interface) <- realizada por <- ControloPersonagem
'''
