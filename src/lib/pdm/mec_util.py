class MecUtil():

    '''
    O Mecanismo Utilidade é responsavel por calcular a utilidade de um estado.
    '''

    def __init__(self, modelo, gama, delta_max):
        self.__delta_max = delta_max
        self.__modelo = modelo
        self.__gama = gama

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
        S, A = self.__modelo.S, self.__modelo.A # quando dize-mos S, A = self.__modelo.S, self.__modelo.A o A fica associado a self.__modelo.S e A a self.__modelo.A
        # S e A sao metodos mas nos queremos queremos a referencia dos metodos, nao queremos invocar o metodo por isso é que não escrevemos S() e A()
        U = {s: 0.0 for s in S()} # aqui sim invocamos a funcao com S()
        # queremos fazer um do while, que nao existe no java, no entanto podemos ter um while que não tem condição final mas tem condição final que será um breack
        while True:
            Uant = U.copy() # copia o objecto
            delta = 0 # iniciar o delta a 0
            for s in S():
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)], default = 0) # se o valor de max for vazio retorna 0 por default, assim não é retornada um exepcao
                delta = max(delta, abs(U[s] - Uant[s])) # aqui já não é preciso exepção dado que tem dodos garantifdamente um valor
            if delta <= self.__delta_max: # como a condição é sair do ciclo (em vez de ficar no ciclo como um ciclo while "normal"), temos de fazer a complementar da informacao que ficaria num ciclo while normal
                break
        return U # retornar U

    def util_accao(self, s, a, U): # nesta funcao vamos calcular a utilidade do estado "s"
        '''
        A utilização vai ser calculada atravez da forma iterativo, cujo o modelo comceptual é quase recursivo
        1. calcular o somatorio da função T(s,a,s')*[R(s, a, s') + (fator de desconto)*U(s')]
        '''
        T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc
        return sum(T(s, a, sn)*R(s, a, sn)+self.__gama * U[sn] for sn in suc(s, a)) # T(s,a,s')*[R(s, a, s') + (fator de desconto)*U(s')]
    # somatorio -> sum


    # descrever o codigo que acabamos de fazer, daquilo que escrevi o que esta certo e o que esta errado

    '''
    Relacao do codigo com o comentarios anterior:

    comecamos por atribuir vareaveis que utilizamos no metodo para reduzir a redundancia e o codigo ser mais claro.
    nao pensei na repeticao da chamada dos metodos S e A.

    se seguida, como descrevi iniciamos o dicionario U com utilidade 0 para cada estado em S

    equecime de referir o do while, esta bastante esplicido no slide de referencia, não foi por nao saber, foi por distracao,
    de qualquer das maneiras o parametro de if condicao ao contrario para o break e sair do while é algo em que não tinha pensado e uma maneira de implementar o do while em python

    Inicializar o Uant com o U.copy, que descrevi correctamente

    Inicializar delta a 0, que tambem fiz correctamente

    Tambem identifiquei o ciclo for de maneira correrta e que deveriamos percorrer os estados em  S

    Identifiquei correctamente o calculo de U[s], no entanto nao consegui identificar a possibilidade de identificar um default
    Essa exprecao precisa de um default porque a funcao A(s) pode nao ter nenhuma accao possivel ou seja nao invoca o metodo util_accao 
    e se nao invoca o metodo util accao não é possivel calcular um max de uma lista que esta vazia, dai a necessidade do default, para 
    que nao seja lancada uma exepcao

    O valore de delta tambem identifiquei correctamente, é o valor maximo entre o delta e modolo de U[s] - Uant[s]

    É feita a verificacao delta <= self.__delta_max e se for verdadeira retornamos U se for falso o ciclo repete-se até que se encontre um delta maior
    '''
    '''
    O metodo util_accao é como descrito calculo do sumatorio da probabilidade de transicao * (recompensa esperada + gama da utilidade so estado sucessor)
    '''