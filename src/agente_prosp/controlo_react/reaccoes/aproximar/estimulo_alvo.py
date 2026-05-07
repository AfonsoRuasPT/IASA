from ecr.estimulo import Estimulo
from sae import Elemento # enumerado da sae

class EstimuloAlvo(Estimulo):

    """
    Detector de estimulos
    """

    def __init__(self, direccao, gama = 0.5):
        self.__direccao = direccao
        self.__gama = gama # gama é a nossa base, sempre inferior a 1

        """
        Quanto maior a gama menos decresce a intencidade do alvo com a distancia.
        E quanto menor mais sensivel se torna a distancia, ou seja, a intencidade do alvo decresce mais rapidamente com a distancia.
        """

    def detectar(self, percepcao):
        """
        Dada um percepcao retorna um float que é a intencidade a que o alvo esta a ser detectado.
        """
        elemento, distancia, _ = percepcao[self.__direccao] # indexação de tublos, como nao nos intereca a orientação do alvo, usamos "_" para ignorar o terceiro elemento do tuplo
        # operador ternario do pyhton

        """
        Retornamos a intenciadade do alvo, que é calculada pela formula gama elevado a distancia, se o elemento detetado for um alvo, 
        caso contrario retornamos 0.
        """
        return self.__gama**distancia \
            if elemento == Elemento.ALVO else 0