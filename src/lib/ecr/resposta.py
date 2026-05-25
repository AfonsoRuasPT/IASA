'''
A Resposta é o elemento da reacção responsável por gerar a acção a executar e definir a sua prioridade.
Define uma resposta a estímulos em termos de acção a realizar e da respectiva prioridade.
A prioridade é definida igual à intensidade do estímulo.
'''

class Resposta: # classe base da biblioteca ECR para respostas a estímulos

    '''
    Resposta define o mecanismo base de geração de uma acção em resposta a um estímulo. 
    Define também a prioridade da acção igual à intensidade do estímulo detectado.

    Resposta é realizada por RespostaMover e RespostaEvitar.
    Resposta tem uma associação com Accao.
    É composta por Reaccao.
    '''

    # Define uma resposta a estímulos, em termos de acção a realizar e da respectiva prioridade

    def __init__(self, accao): # recebe a acção base que esta resposta irá devolver
        self._accao = accao 

    def activar(self, percepcao, intencidade = 0): # activa a resposta, define a prioridade e devolve a acção
        accao_atual = self._obter_accao(percepcao) # obtém a acção consoante a percepcao
        
        if accao_atual is not None: # verifica se existe uma acção válida
            accao_atual.prioridade = intencidade # define a prioridade da acção igual à intensidade do estímulo detectado
        return accao_atual # devolve a acção com a prioridade definida

    def _obter_accao(self, percepcao): # método protegido, devolve a acção
        return self._accao 