from pee.larg.procura_largura import ProcuraLargura 

from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.prof.procura_pro_iter import ProcuraProIter
from pee.prof.procura_prof_lim import ProcuraProfLim

from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.melhor_prim.procura_informada import ProcuraInformada

from mod_prob.problema_contagem.problema_contagem import ProblemaContagem

from mod_prob.heuristica_de_contagem import HeuristicaDeContagem

MECANISMOS_PROCURA = [
    ProcuraProfundidade(),
    ProcuraLargura(),
    ProcuraCustoUnif(),
    ProcuraProIter(),
    ProcuraProfLim(),
    ProcuraAA(),
    ProcuraSofrega()
]

VALOR_INICIAL  = 0
VALOR_FINAL = 8
INCREMENTOS = [1, 2, 3]
INCREMENTOS_CICLO = [1, 2, 3, -1]


def teste_contagem(valor_inicial, valor_final, incrementos, mecanismos_procura):
    print()
    print("Valor inicial: ", valor_inicial)
    print("Valor final: ", valor_final)
    print("Incrementos: ", incrementos)

    problema = ProblemaContagem(valor_inicial, valor_final, incrementos)

    for mec_proc in mecanismos_procura:
        if isinstance(mec_proc, ProcuraInformada):
            heuristica = HeuristicaDeContagem(valor_final)
            solucao = mec_proc.procurar(problema, heuristica)
        else:
            solucao = mec_proc.procurar(problema)

        print()
        print(mec_proc.__class__.__name__)
        print("Solução: ", [passo.operador.incremento for passo in solucao])
        print("Dimensão: ", solucao.dimensao)
        print("Custo: ", solucao.custo)

###

print("\nTeste sem ciclos")
teste_contagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS, MECANISMOS_PROCURA)

#print("\nTeste sem ciclos")
#teste_contagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS_CICLO, MECANISMOS_PROCURA[1:]) # NÃO PODEMOS TESTAR A PROCURA EM PROFUNDIDADE