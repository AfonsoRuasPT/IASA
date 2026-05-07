from sae.ambiente.elemento import Elemento

class MecDelib():

    """
    O MecDelib centraliza o raciocínio sobre os fins do agente. Conforme dita a arquitetura, 
    atua diretamente sobre os dados do ModeloMundo para avaliar o ambiente circundante e 
    decidir quais os estados específicos que constituem as metas de exploração.
    """

    def __init__(self, modelo_mundo):

        """
        O construtor estabelece a ligação fundamental ao ModeloMundo, guardando esta referência 
        num atributo privado para uso posterior nas fases de geração e seleção de objetivos 
        representadas no diagrama UML.
        """
        self.__modelo_mundo = modelo_mundo

    def deliberar(self):

        """
        Método público que concretiza o processo de deliberação. Orquestra as chamadas 
        internas começando por invocar o método privado gerar_objectivos e passando o 
        resultado diretamente para o método selecionar_objectivos, devolvendo a lista 
        final de instâncias de EstadoAgente ao controlo deliberativo.
        """

        objectivos = self.__gerar_objectivos() # geramos todos os objectivos
        if objectivos: # verificamos se existem objectivos
            return self.__seleccionar_objectivos(objectivos) # e retornamos todos os objectivos

    def __gerar_objectivos(self):

        """
        Método privado responsável por percorrer o conjunto de estados fornecido pelo 
        ModeloMundo e identificar aqueles que albergam elementos de interesse, criando 
        uma lista inicial de potenciais EstadoAgente a explorar.
        """
                
        return [estado for estado in self.__modelo_mundo.obter_estados()
                if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
        # verificamos se o elemento ]e um alvo e se for defenimos como um objetivo

    def __seleccionar_objectivos(self, objectivos):

        """
        Recebe a lista de objetivos brutos gerada anteriormente e aplica critérios de 
        filtragem ou priorização, retornando a lista refinada de EstadoAgente que o 
        planeador deverá posteriormente processar.
        """

        objectivos.sort(key =self.__modelo_mundo.distancia)
        # uma coias é a invocacao de uma funcao outra é a funcao em si,

        """
        Fazemos isto porque o parâmetro key do sort precisa de receber a referência de uma função, e não o seu resultado. 
        Quando escrevemos .distancia sem os parênteses, estamos a entregar as "instruções" ou a "ferramenta" de cálculo ao sort. 
        Com essa ferramenta na mão, o próprio sort vai encarregar-se de pegar em cada item da lista objectivos e aplicá-lo na 
        função, um por um, para descobrir o valor de ordenação de cada elemento. 
        """
        
        return objectivos[:1]
        # com este sort pretendemos que dentro dos objetivos (alvos) que verificamos
        # retornamos o objetivo mais proximo, ou seja que tem menos distancia a nossa posicao
        # dependendo do problema podemos defenir o objectivo de forma diferente.