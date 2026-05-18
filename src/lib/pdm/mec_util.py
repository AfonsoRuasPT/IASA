class MecUtil():

    def __init__(self, modelo, gama, delta_max):
        self.__delta_max = delta_max
        self.__modelo = modelo

    def utilidade(self):
        '''
        1. inicializar um dicionario U(s) com cumprimento de S (conjunto de estados do mundo que podemos ir buscar fazendo self.__modelo.S()) cujaos elementos sao x e y, em que x é o estado e y é a utilidade, e inicializar a lista com utilidades todas a 0
        2. faz: 2.1. atribui o valor de U a vareavel Uant (Uant = U não funciona,  deve criar um novo dicionario que tem o conteudo do dicionario, deve ficar: Uant = U.copy()) - copy primeiro nivel de daos; deep copy sao todos os niveis de dados
                2.2. atribui o valor de 0 a delta (mesmo que acontece em cima)
                2.3. para cada s (estado) em S (conjunto de estados)
                    2.3.1. calcula a utilidade maxima da accao de cada estado "s" chamando util_accao e passando as vareaveis (s, a, Uant) e atribuimos esse valor ao dicionarios na possicao correspondente ao estado
                    2.2. atribui a vareavel delta ao maior valor entre delta e o modulo da subtracao da Utilidade e a Utilidade anterior do estado "s"
        3. verifica se delta é maior do que a vareavel delta_max, se for volta para o ponto 2, se não vai sai do loop
        4. retorna o valor de U que é o dicionarios da utilidade
        '''
        

    def util_accao(self, s, a, U): # nesta funcao vamos calcular a utilidade do estado "s"
        '''
        A utilização vai ser calculada atravez da forma iterativo, cujo o modelo comceptual é quase recursivo
        1. calcular o somatorio da função T(s,a,s')*[R(s, a, s') + (fator de desconto)*U(s')]
        '''