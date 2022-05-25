'''Troco em Moedas
O caixa de um supermercado precisa dar o troco de x centavos.  Sabendo que as moedas disponíveis no caixa são de R$ 0,50, R$ 0,25, RS 0,10, R$ 0,05 e R$ 0,001, elabore uma função chamada troco que receba o valor inteiros x, do troco em centavos, como parâmetro e imprima a quantidade de moedas de 50, 25, 10, 5 e 1 centavos que deve dar, de forma a minimizar a quantidade de moedas do troco.

A Entrada consiste de:
A função troco deve ser chamada para qualquer valor arbitrário de troco definidos nos casos de teste, que é um número inteiros x, o valor do troco em centavos.

A Saída deve apresentar:
A função troco deve imprimir a quantidade de moedas de cada valor em centavos que serão entregues como troco, sempre com o menor número de moedas possíveis.
Por exemplo, para um troco de R$ 0,79 deve imprimir:
1 moedas de R$ 0,50
1 moedas de R$ 0,25
0 moedas de R$ 0,10
0 moedas de R$ 0,05
4 moedas de R$ 0,01

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.
Faça um algoritmo que funcione apenas para os valores de moedas do problema, assim a função que você irá implementar precisará usar apenas o conhecimento que você aprendeu até o presente momento na disciplina. Não use comandos e instruções que ainda serão ensinados em lições futuras.

Descrição dos Exemplos:
Os exemplos do Moodle são autoexplicativos.
'''


def troco(n):
    qtd_de_50 = n // 50
    qtd_de_25 = (n - (qtd_de_50 * 50 )) // 25
    qtd_de_10 = (n - ((qtd_de_50 * 50 ) + (qtd_de_25 * 25 ))) // 10
    qtd_de_5 = (n - ((qtd_de_50 * 50 ) + (qtd_de_25 * 25 ) + (qtd_de_10 * 10 ))) // 5
    qtd_de_1 = (n - ((qtd_de_50 * 50 ) + (qtd_de_25 * 25 ) + (qtd_de_10 * 10 )+(qtd_de_5 * 5 ))) // 1

    print(f'{qtd_de_50} moedas de 50 centavos')
    print(f'{qtd_de_25} moedas de 25 centavos')
    print(f'{qtd_de_10} moedas de 10 centavos')
    print(f'{qtd_de_5} moedas de cinco centavos')
    print(f'{qtd_de_1} moedas de 1 centavo')
