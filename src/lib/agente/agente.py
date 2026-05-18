'''
O projeto que estamos a desenvolver é um projeto de elevada complexidade, que requer atenção e conhecimento.
Todo o codigo desenvolvido nas 4 partes do projeto será feito com base nos conhecimentos adquiridos em aula,
quer seja conhecimentos de teoria ou sintaxe de python e tambem em acompanhamento com o professor e dos PDF´s que ditam a arquiterura de cada parte do projeto.
'''

'''
A complexidade é a dificuldade em compreender/relacionar as partes de um sistema. Depende então da dificuldade do problema, do numero de classes e relações entre elas e do nivel de
conhecimento necessario para o seu desenvilvimento.

No pdf "Introdução à engenharia de software" nos slides 5 e 6 podemos observar imagens que retratam justamente o que é acomplexidade. Na primeira imagem observamos 9 classes e as suas
12 relações estre elas, já no slide 6 observamos uma quantidade absulda de classes e relacoes, não se percebe nada. O desenvolvimento do projeto nesse slide é muito elevado dada nao so 
a complexidade mas tambem a falta de organização.
A complexidade cresce exponencialmente uma vez que quando o numero de classes aumenta o numero das suas relacoes aumenta muito mais.
Isto realça a importancia da oragnização.
Existe complexidadde desorganizada onde xiste ordem, organização, função, propósito em cada linha de codigo escrita e existe complexidade desorganizada a desordem, desorganização,
perda de função e de propósito são evidentes. A imagem do pdf "Introdução à engenharia de software" slide 9 retrata muito bem estas diferenças.

A mudança é a a velocidade a que o software evolui ou é alterado com o objetivo de atingir as funcionalidades pretendidas para o projeto. 
'''

'''
A engenharia de software especializa-se na criacao de softwere complexo e de qualidade. Para isso o softwere de ve ser desenvolvido de forma sistematico e quantificavel.

Sistematico: desenvolver software de forma organizada e previsível
Quantificavel: capacidade de avaliar os meios envolvidos e os resultados produzidos assim como garantir a qualidade e o desempenho do software produzido. Importante para garantir 
que os requesitos do projeto são cumpridos.
'''

'''
Como referido anteriormente a complexidade de um projeto deve ser sempre organizada, e para isso devemos sempre seguir os principios de abstracao e modularização.
Abstração : identificação de caracteristicas comuns e omitir detalhes não relevantes. Desenvolver as coisas de maneira progreciva.
A abstrção não "retira" complexidade ao projeto, simplesmente permite com que consigamos olhar para um problema grande e complexo em varios pequenos problemas mais simples e faceis.
Devemos olhar para o problema e identificar as partes em que o problema se divide e depois olhar para cada parte individual e se possivel dividir outra vez em problemas mais pequenos,
detalhando cada vez mais a solucao. Para isso usamos ferramentas como a simplifocação, focagem e modelos que nos permitem reduzir a complexidade da descrição, focar nos as petos mais
relevantes e fazer descrições abstratas do sistema respetivamente. O que acabei de descrever encontrase de forma simples demostrado no slide 12 
'''

'''
Modularização: divisão do sistema, cada perte tem uma função clara e bem defenida.

o projeto embora de extrema complexidade esta muito bem organizado, seguinto estes conceitos de engenharia de software e detalhado na arquitetura atravez da linguagem UML, 
(Unified Modeling Language).
Esta linguagem tem varios tipos de diagramas, diagramas de classes, diagramas de sequencia e diagramas de atividade.
Diferentes diagramas mostam perspectivas diferentes entre si, podem ser estruturais e comportamentais.

Estrutural: mostra as partes do sistema e as suas relações
Comportamental: mostra o comportamento dinamico do sistema e como as partes se interagem e evoluem ao longo do tempo.

Esta class Agente esta inserida num diagrama de classes.
Os diagramas de classes descrevem a organização estática de um sistema, quais as partes que existem e como se relacionam entre si.

A class pode ser absrata se tiverem um bola no canto superior direito, ou seja uma class abstrata é uma class que nao pode ser instanciada, é como se fosse um contrato que obriga
as classes que a concretizam a implementar os seus metodos abstratos.

As relações entre classes são representadas por linhas que se ligam com simbolos que indicam o tipo de relação:

Associação: Linha contínua.  
Dependência: Linha tracejada com seta aberta.  
Agregação: Linha contínua com losango vazio.  
Composição: Linha contínua com losango preenchido.  
Generalização (Herança): Linha contínua com seta.  
Realização (Interface): Linha tracejada com seta.  

Podemos tambem observar os atributos da class com um + (publico), - (privado) e # (protected)
Podemos observar os metodos se sao publicos privados ou protected tambem (usa os mesmos simbolos) e se sao abstratos (italico), o que recebem como parametros e o que retornam.
'''

from abc import abstractmethod, ABC # importar a biblioteca abc porque no python é assim que se simula uma interface

class Agente(ABC): # Agente herda de ABC para ser uma class abstracta

    '''

    Agente é uma representação computacional de um sistema autónomo que opera no ciclo percepção→processamento→acção.
    Esta classe implementa esse ciclo: _percepcionar obtém informação do ambiente, _controlo.processar decide a acção, e _actuar executa-a. 
    O agente é reactivo ou seja responde a estímulos do ambiente e autónomo porque executa o ciclo sem intervenção externa.

    Agente tem uma relação de agregação com o Controlo.
'''

    def __init__(self, controlo): # def __init__ é o construtor da class Agente, este metodo é chamado automaticamente quando um objeto desta class é criado.
        # PYTHON – atributo protegido (convenção de um underscore "_")
        # Um único "_" antes do nome indica que o atributo é protegido, pode ser acedido nesta class e nas subclasses
        self._controlo = controlo

    @abstractmethod # metodo abstrato, que significa que tem de ser implementado por qualquer class que concretize esta interface
    def _percepcionar(self):
        """Obter percepção do ambiente. Retorna uma percepção""" # a docstring entre """ """ funciona como documentação do método


    @abstractmethod
    def _actuar(self, accao): # este metodo deve executar a accao no ambiente
        """Actua"""

    def executar(self): # este me todo executa o ciclo de percepção-processamento-acção

        percepcao = self._percepcionar() # obtém percepção do ambiente chamando o método abstracto da subclasse

        accao = self._controlo.processar(percepcao) # delega a decisão ao Controlo, padrão de delegação: Agente utiliza Controlo processar, mantendo acoplamento baixo

        if accao is not None: # None é o valor que indica ausência de acção; usa-se "is not None" em vez de "!= None" porque é uma comparação de identidade (é o mesmo objecto None), não de valor
            return self._actuar(accao) # executa a acção concreta na subclasse
        return None # sem acção válida, o ciclo termina sem efeito

        """Executar acção no ambiente. Falta implementar o método executar da Classe Agente"""
        # raise NotImplementedError para dar erro caso o método seja chamado sem ser implementado