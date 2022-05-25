'''
Soma Harmonica
Uma série harmônica é uma soma infinita, definida pela seguinte fórmula:

∑∞k=11k=1+12+13+14+...

Recursivamente, é possível encontrar a soma harmônica dos X primeiros elementos da série, da seguinte forma:

soma–harmonica(X)={11X+soma–harmonica(X-1)se X=1se X>1

Dessa forma, crie uma função soma_harmonica(X) que calcule recursivamente a soma harmônica de X-1 elementos.

A Entrada consiste de:
O único parâmetro da sua função será o valor X≥1.

A Saída deve retornar:
A soma harmônica de x-1 elementos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.
'''
def soma_harmonica(x):
    return 1 if x == 1 else (1/x) + soma_harmonica(x-1)

