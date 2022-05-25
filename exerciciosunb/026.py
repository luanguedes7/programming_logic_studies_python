'''
Sequências de pares v2
Implemente uma função recursiva chamada paresDeNumeros que receba dois números inteiros n e m, em que n+1<m. A função deve imprimir pares de números inteiros nimj, em que ni=ni−1+2 e mj=mj+1−1, enquanto ni≤mj. Considere que n0=n e m0=m.

A Entrada consiste de:
A função paresDeNumeros recebe como parâmetros dois números inteiros positivos n e m (1≤n≤109−2,n<m≤109).

A Saída deve apresentar:
Imprima os termos que compõem a sequência de pares de números supracitada, sendo que cada par de números deve ser impresso em uma única linha e esses números devem estar separados por um espaço em branco.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, a função recebe n = 1 e m = 10 e como n < m, prossegue para segunda rodada com 3 e 9. Como n < m, prossegue para terceira rodada com 5 e 8. Como n < m, prossegue a quarta rodada com 7 e 7, mas são iguais a função para a execução e não apresenta nada.
'''
def paresDeNumeros(n, m):
    if n == m:
        print(n,  m)
    elif n > m:
        pass
    else:
        print(n, m)
        paresDeNumeros((n + 2), (m - 1))

paresDeNumeros(1,10)
paresDeNumeros(3,19)
paresDeNumeros(10,12)
