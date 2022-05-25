'''
Múltiplos
Uma operação bastante comum dados dois números a e b é saber se a é um múltiplo de b ou não. Formalmente, um inteiro a é múltiplo de um inteiro b se existe um inteiro k tal que b*k=a.

Nesse exercício, você deve criar uma função chamada multiple, que recebe dois inteiros, a e b. A função deve imprimir na tela "a eh multiplo de b", caso a seja multiplo de b; "b eh multiplo de a" caso b seja multiplo de a; "nao multiplos" em quaisquer outros casos. Substitua a e b pelo valor dos argumentos para imprimir. Imprima SEM as aspas. Veja os exemplos.

Dica: Python possui o operador '%' (módulo). Ela retorna o resto da divisão inteira de um número por outro (e.g. 2 % 10 dá como resultado o resto da divisão de 2 por 10).

A Entrada consiste de:
Os parâmetros da função multiple que são os dois números inteiros a e b (-10000≤a,b≤10000).

A Saída deve apresentar:
"a eh multiplo de b", caso a seja multiplo de \(b\); "b eh multiplo de a" caso b seja multiplo de a; "nao multiplos" em quaisquer outros casos. Substitua a e b pelo valor dos argumentos para imprimir. Imprima SEM as aspas.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro e segundo exemplos, 6 é múltiplo de 2, então a função imprime "6 eh multiplo de 2".
No terceiro exemplo, nem 21 é múltiplo de 22, nem 22 de 21, então a função imprime "nao multiplos".
'''
def multiple(a, b):
    if (a % b) == 0:
        print(f'{a} eh multiplo de {b}')
    elif (b % a) == 0:
        print(f'{b} eh multiplo de {a}')
    else:
        print('nao multiplos')
