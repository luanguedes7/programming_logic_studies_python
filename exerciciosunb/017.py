'''
Longevidade na UnB I
O Decanato de Graduação (DEG) está testando uma nova funcionalidade no SIGAA que permite apresentar a quantidade de períodos que um determinado estudante já concluiu na Universidade de Brasília. Para isso, o DEG aproveita as informações de ingresso na UnB existentes no próprio número de matrícula dos alunos e compara com o ano e o semestre atual. Como se sabe, os quatro dígitos mais significativos d1,d2,d3 e d4 do número de matrícula indicam o ano e o semestre de ingressos do aluno na UnB.

Por exemplo, se o número de matrícula de um estudante é 190199999, os quatro dígitos mais significativos formam o número 1901, em que adota-se a convenção (d1=1,d2=9,d3=0,d4=1). O número formado da combinação de d1 e d2, 19, indicam que o aluno ingressou na UnB em 2019 e o d4=1 mostra que o aluno ingressou no segundo semestre desse ano. Outro exemplo se trata do número de matrícula 180099899, que indica que estudante ingressou na UnB no primeiro semestre de 2018.

Elabore uma função chamada quantosSemestres que receba como parâmetros três números inteiros m, a e s associados ao número de matrícula do aluno, o ano atual e o semestre atual, respectivamente. Essa função deve calcular a quantidade mínima de semestres (concluídos) em que o referido aluno está na UnB.

A Entrada consiste de:
A entrada compreende os parâmetros da função quantosSemestres que são três números inteiros m, a e s (100000000≤m≤500000000,2010≤a≤2050,s∈{0,1} ) associados ao número de matrícula do aluno, o ano atual e o semestre atual, respectivamente. É garantido que o ano e o semestre atual do aluno são maiores ou iguais ao ano e semestre de ingresso na UnB.

A Saída deve apresentar:
A função quantosSemestres deve imprimir a quantidade mínima de semestres em que o aluno associado ao número de matrícula está na UnB.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, de acordo com o número de matrícula, o aluno ingressou na UnB no primeiro semestre de 2020 e o semestre atual também é o primeiro semestre de 2020. Portanto, o aluno ainda não concluiu nenhum semestre.
No segundo exemplo, de acordo com o número de matrícula, o aluno ingressou na UnB no primeiro semestre de 2020 e o semestre atual é o segundo semestre de 2020. Portanto, o aluno concluiu um período na UnB.
'''


def quantosSemestres(m, a, s):
    d1, d2, d3, d4, d5, d6, d7, d8, d9 = list(str(m))
    ano_de_entrada = int('20' + d1 + d2)
    semestre_de_entrada = int(d3 + d4)

    qtd_de_anos = a - ano_de_entrada
    qtd_de_semestres = (qtd_de_anos * 2) - (semestre_de_entrada - s)

    print(qtd_de_semestres)


