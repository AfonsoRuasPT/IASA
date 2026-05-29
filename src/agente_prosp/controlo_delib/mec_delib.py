from sae.ambiente.elemento import Elemento

'''
Na Parte 4 do nosso projeto introduzimos a arquitectura deliberativa, que a ocontrario da reactiva que só reage a estimulos, o agente deliberativo tem memória de representação 
interna do mundo e consegue simular o futuro para antecipar estados e gerar planos de acção óptimos.

O processo de tomada de decisão segue o ciclo:
  1 - Observar o mundo, gera percepções
  2 - Actualizar o modelo do mundo, com base nas percepções
  3 - Deliberar - decidir o que fazer, gera objectivos
  4 - Planear - decidir como fazer, gera plano de acção
  5 - Executar o plano
 
O planeamento é feito com base em Procura em Espaço de Estados (PEE).
O espaço de estados é uma abstracção do domínio do problema onde cada configuração possível é representada como um estado, como visto na Parte1, e as acções que mudam de configuração
são representadas como operadores que originam transições de estado.
A solução é um percurso no espaço de estados do estado inicial até ao estado objectivo.
'''

class MecDelib():

    def __init__(self, modelo_mundo):

        """
        O Mecanismo de Deliberativo é a componente que delibera, ou seja, decide os objectivos e que objectivo deve ser o estado_final
        Consulta o ModeloMundo para identificar os estados que representam alvos no ambiente e selecciona o mais próximo como objectivo a 
        atingir.
        O resultado é passado ao Planeador que decide a melhor maneira de atingir esse objectivo.

        MecDelib tem uma associação com ModeloMundo.
        Compoe ControloDelib.
        """

        self.__modelo_mundo = modelo_mundo

    def deliberar(self):

        """
        Coordena o processo de deliberação, gera todos os objectivos possíveis e selecciona os mais relevantes. 
        Devolve a lista final de EstadoAgente objectivo ao ControloDelib.
        """

        objectivos = self.__gerar_objectivos() # geramos todos os objectivos
        if objectivos: # verificamos se existem objectivos # := self.__gerar_objectivos nota que estava escrito no codigo do professor, comentar depois o que é em python
            return self.__seleccionar_objectivos(objectivos) # chama a funcao __seleccionar_objectivos que retorna o objectivo mais proximo

    def __gerar_objectivos(self):

        """
        Percorre todos os estados válidos do ModeloMundo e identifica os que sao ALVO
        """
                
        return [estado for estado in self.__modelo_mundo.obter_estados()
                if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
        # verificamos se o elemento é um alvo e se for defenimos como um objetivo, fica na lista

    def __seleccionar_objectivos(self, objectivos):

        """
        Ordena os objectivos por distância ao estado actual do agente e devolve apenas o mais próximo. 
        A escolha do objectivo mais próximo é como se fosse uma heurística de selecção que pode ser ajustada conforme o problema.
        """

        objectivos.sort(key =self.__modelo_mundo.distancia)
        # uma coias é a invocacao de uma funcao outra é a funcao em si,
        """
        Fazemos isto porque o parâmetro key do sort precisa de receber a referência de uma função, e não o seu resultado. 
        Quando escrevemos .distancia sem os parênteses, estamos a entregar as "instruções" ou a "ferramenta" de cálculo ao sort. 
        Com essa ferramenta na mão, o próprio sort vai encarregar-se de pegar em cada item da lista objectivos e aplicá-lo na 
        função, um por um, para descobrir o valor de ordenação de cada elemento. 
        """
        
        return objectivos # alterado na aula de entrega 12
        # com este sort pretendemos que dentro dos objetivos (alvos) que verificamos
        # retornamos o objetivo mais proximo, ou seja que tem menos distancia a nossa posicao
        # dependendo do problema podemos defenir o objectivo de forma diferente.