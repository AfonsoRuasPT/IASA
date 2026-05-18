from .evento_jogo import EventoJogo


class AmbienteJogo():

    '''
    AmbienteJogo é o ambiente virtual do jogo onde a personagem actua.
    Gera eventos (percepções) e recebe comandos (acções) da personagem.

    AmbienteJogo agrega EventoJogo: mantém um dicionário com todos os EventoJogo possíveis e o evento actual.
    '''

    def __init__(self):
        self.__eventos = {evento.value: evento for evento in EventoJogo} # enumerado de eventos do jogo
        """seja um dicionaria ou uma lista quando defenimos cada elemento, e geramos dinamicamente as expressoes de
          cada elemento, ou seja, o valor de cada elemento do enumerado, e o proprio elemento do enumerado, entao 
          temos um dicionario que mapeia os valores dos eventos do jogo para os próprios eventos do jogo, o que permite 
        acessar os eventos do jogo a partir dos seus valores, defenidos no enumerado EventoJogo"""
        
        self.__evento = None # evento atual do jogo
    # criar enumerado envento jogo


    def evoluir(self):
        # atualizar evento com o gerar evento
        self.__evento = self.__gerar_evento() # atualizar o evento atual do jogo com o evento gerado pelo método _gerar_evento, que é um método privado para gerar um evento do jogo, é chamado pelo método evoluir para atualizar o evento atual do jogo
        if self.__evento is not None: # se o evento gerado for diferente de None, ou seja, se houver um evento do jogo a atualizar, None é uma marca de ausencia de valor, o != implica comparacao de valores ent aqui n dá, é um teste semantico
            self.evento.mostrar() # imprimir o evento atualizado do jogo

    def observar(self):
        #retorna o atributo envento privado
        return self.__evento
    
    def executar(self, comando):
        #sobre o comando, chama o metodo mostrar
        comando.mostrar() # mostrar o comando do jogo
        
    def __gerar_evento(self): # metodo privado para gerar um evento do jogo, é chamado pelo método evoluir para atualizar o evento atual do jogo
        texto = input("\nEvento? ")  # solicitar ao utilizador que digite o evento do jogo
        return self.__eventos.get(texto) # retornar o evento do jogo correspondente ao texto digitado pelo utilizador, utilizando o dicionario de eventos do jogo para mapear o texto para o evento correspondente
    """utilizando o get(texto), em vez do [texto], permite retornar None caso o texto digitado pelo utilizador não 
    corresponda a nenhum evento do jogo, evitando assim um erro de chave inexistente no dicionario de eventos do jogo"""


    @property
    def evento(self): # implementacao do metodo evento para retornar o evento atual do jogo, é um getter para o atributo privado __evento, que é onde se guarda o evento atual do jogo
        return self.__evento
    """temos sempre um atributo private, a propriedade é que é publica, e a propriedade retorna como valor o atributo privado interno"""
