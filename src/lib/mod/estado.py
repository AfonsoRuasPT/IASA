from abc import abstractmethod

'''
Mecanismo de Procura em Espaços de Estados (PEE).

O Raciocínio Automático é a capacidade de um sistema computacional resolver de forma automática um problema com base numa
representação de conhecimento do domínio, produzindo uma solução a partir de diversas alternativas possíveis. O processo envolve:
  Exploração de opções - raciocínio prospectivo, simulação interna do domínio
  Avaliação de opções - custo (recursos necessários) e valor (utilidade)

O Modelo do Problema é a representação interna que suporta
o raciocínio automático e é composto por três elementos fundamentais:
  Estado    - representa uma configuração (situação) do problema
  Operador  - representa uma acção (transformação de estado)
  Problema  - estado inicial + operadores + função objectivo

O Espaço de Estados é o conjunto de todos os estados possíveis e das transições entre eles, representado sob a forma de um grafo.
A solução é um percurso nesse grafo do estado inicial ao estado objectivo.
'''

class Estado():

    '''
    Estado representa uma configuração (situação) possível na resolução do problema (slide 9 Parte3). Cada estado tem identificação única gerada por 
    id_valor(), que é usada pelo mecanismo de procura para comparar estados e verificar eficientemente se um estado já foi explorado anteriormente,
    evitando ciclos e desperdício de memória.

    Estado é usado por Problema.objectivo() para verificar se é o estado final.
    '''

    """
    A classe Estado é a unidade de informação mais elementar do sistema, serve para representar uma única situação, momento ou 
    configuração do tabuleiro dentro da resolução do seu problema. O seu método id_valor tem a função de gerar e devolver uma 
    identificação única, assim como os metodos internos hash e eq que atribuem o id ao objeto e verifica a igualdade respetivamente. 
    
    Esta identificação é o que vai permitir ao mecanismo de procura comparar diferentes momentos e perceber de forma eficiente se 
    um determinado estado já foi explorado anteriormente, sendo vital para evitar que o algoritmo ande em círculos ou gaste memória
    desnecessária.
    """

    def __hash__(self): #  método especial invocado por hash(estado) e ao usar o estado como chave de dicionário
        return self.id_valor() # delega o cálculo do hash ao método abstracto id_valor()
        # permite que Estado defina a sua própria forma de identificação única
    
    def __eq__(self, objeto): # método especial invocado pelo operador "==" entre dois estados
        if isinstance(objeto, Estado): # verifica se o objecto comparado é também um Estado
            return self.__hash__() == objeto.__hash__() # dois estados são iguais se tiverem o mesmo id_valor (mesmo hash)
        else:
            return False # objectos de outros tipos nunca são iguais a um Estado

    @abstractmethod
    def id_valor(self): # método abstracto: cada subclasse define como calcular o identificador único do seu estado
        """"""