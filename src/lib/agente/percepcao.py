'''
A dinâmica de um sistema é a forma como ele evolui ao longo do tempo.
O comportamento de um sistema computacional depende de duas coisas: entradas,o que vem do exterior, e do seu estado interno atual. Com base nisto, o sistema passa por uma função
de transformação que vai gerar as saídas (o que o sistema faz) e ditar qual será o seu próximo estado.

Nos slides 4 e 5, isto é formalizado através do conceito de Máquinas de Estados (no nosso caso, Máquinas de Estados Finitos, pois a memória dos computadores obriga a que o número de 
estados não seja infinito).
Existem duas abordagens teóricas para a função de saída as Máquinas de Mealy onde a saída depende tanto do estado atual como das entradas e as Máquinas de Moore onde a saída depende 
única e exclusivamente do estado em que o sistema se encontra.
'''

'''
O Modelo de dinamica de um sistema representa todos os estados possoveis que o sistema pode vir a ter.
Ambos o espaco de estados e o espaco de fases sao maneiras de representar a evolução de um sistemas e podemos observar os seus graficos no slide 10.
A evolução de um estado pode ser vista como uma trajetória que descreve padroes. Se os valores do sistema forem contínuos, chamamos a isso um espaço de fase.
Como é impossível e desnecessário modelar cada pequeno valor contínuo na programação, usamos a abstração. Por exemplo, em vez de medirmos cada grau exato, criamos "estados abstratos" 
como "Céu Limpo" ou "Céu Nublado". A passagem de um estado para o outro (a transição) acontece apenas quando ocorre um evento específico que cruza um certo limite (threshold).
'''

'''
Para representar esta dinâmica visualmente na nossa arquitetura, usamos os Diagramas de Transição de Estado em UML (slide 12 e 13).
No exemplo prático do jogo (slides 7 a 9 e 14), temos a nossa personagem (agente) que tem o objetivo de fotografar animais. Podemos assumir diferentes estados: "Procura", "Inspecção",
"Observação" ou "Registo".

Neste diagrama UML, usamos um círculo preto para indicar o Início (Nó inicial) e um círculo preto com uma borda para o Fim (Nó final).
Os retângulos com cantos arredondados são os Estados.
As setas que ligam os estados representam as Transições. Para uma transição acontecer, é preciso que ocorra um Evento (por exemplo, a personagem ouvir um ruído). 
'''

from abc import ABC, abstractmethod

class Percepcao(ABC):

    '''
    A Percepção é a informação que o agente recolhe do ambiente.
    Percepção não tem atributos nem métodos, serve apenas para definir um tipo de objeto, Percepcao.

    Associação com PercepcaoJogo.
    '''

    """Interface que representa uma percepção"""