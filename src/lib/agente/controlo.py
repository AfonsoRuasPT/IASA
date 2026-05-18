'''
Para reduzir a complexidade desorganizada e controlar a organizada, usamos três vertentes principais: métricas, princípios e padrões.

As métricas servem para quantificar e avaliar a qualidade da nossa arquitetura. 

Acoplamento: É o grau de interdependência entre as diferentes partes do sistema. O nosso objetivo no projeto deve ser manter o acoplamento o mais baixo possível, para que o código
seja fácil de manter e evoluir. No slide 5 vemos claramente que uma relação de herança gera o nível mais alto de acoplamento, enquanto uma simples relação de dependência é muito mais
fraca e flexível.

Coesão: É o oposto, foca-se no interior do próprio módulo (packages). Refere-se à coerência dos elementos agrupados numa classe ou função. A coesao deve ser elevada. 
Um módulo coeso que faz a sua função de forma clara é mais fácil de compreender e reutilizar noutras partes do código.
'''

'''
Para garantir que atingimos este baixo acoplamento e alta coesão, temos de nos guiar pelos princípios da Modularização e da Fatorização.

A modularização divide-se essencialmente em decomposição e encapsulamento. A decomposição serve para partir o sistema em partes coesas.
O encapsulamento serve para isolar os detalhes internos das nossas classes em relação ao exterior. Devemos aceder e interagir com as diferentes partes apenas através de interfaces,
o que reduz muito as dependências do código. Por exemplo dentro de um carro o condutor consegue abrir/fechar os vidros de todos os passageiros mas so ele é que consegue aceder ao seu
proprio vidro. Este incapsulamente é muito util, o condutor é a class pai e consegue "mescer" nos vidros dos passageiros. Vidro do passageitos sao protected porque o condutor e eles
podem alterar, e o vidro do condutor é private so ele pode mescer. Isto faz sentido porque o condutor é o responsavel pelo carro e apela segurança. Pode ser perigoso se um passageiro
podesse mescer no vodro do condutor.

A fatorização é o princípio que nos ajuda a eliminar a redundância (código repetido). A redundância é uma das maiores causas de complexidade desorganizada. Podemos extrair este código
comum de duas formas: por Herança (acoplamento alto) ou por Delegação (class usa e delega funções para outra, acoplamento baixo).
'''

'''
Um projeto funciona por fases iterativas que passam pela arquitetura estrutural e pela implementação comportamental. 
O comportamento é como o nosso sistema atua dadas certas entradas e o seu estado atual, evoluindo no tempo.

Os Diagramas de Atividade descrevem o fluxo de controlo, ou seja, a sequência de ações necessárias para realizar uma função.
Estes diagramas usam "nós" gráficos: 
Ações: tarefas atómicas.
Nós de início e fim da atividade.
Decisões representadas por losangos para decidir que fluxo o código vai seguir.

Um recurso muito interessante são as Partições de execução (slide 17). São organizadas visualmente e servem para dividir responsabilidades. Podem ser usadas para separar, por exemplo,
qual é a ação que pertence ao Agente (personagem) e qual pertence ao Controlo. Também podemos desenhar "fluxos de objetos" a "viajar" entre estas atividades para representar a 
transferência de dados.
'''

'''
O Diagrama de Sequência mostra acomunicação entre partes do projeto numa linha temporal.

Nestes diagramas temos as Linhas de vida (lifelines) a descer verticalmente para representar a passagem do tempo. Os retângulos nessas linhas são os Focos de ativação, que indicam que
uma operação está efetivamente a ser executada. As classes/objetos interagem através de setas horizontais. 

Para lidar com lógicas de código nestas trocas de mensagens usamos Operadores (fragmentos de interação). Por exemplo, o "alt" serve para seleções alternativas (como um if/else 
dependendo se uma impressora está ocupada ou livre, como no exemplo do slide 23), o "loop" para repetições ect..
'''

from abc import ABC, abstractmethod

class Controlo(ABC):

    '''
    A class Controlo como indica o nome controla oa gente e processa as percepcoes do ambiente do agente e retorna a accao que o agente deve fazer. 
    É o "cerebro" do agente implementa a lógica de decisão.

    Controlo tem uma relação de dependencia com Accao e Percepcao.
    '''

    @abstractmethod
    def processar(self, percepcao):
        """Processar a percepção e retornar uma acção."""
