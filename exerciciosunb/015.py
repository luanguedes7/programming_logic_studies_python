'''
Equação
O programa abaixo deve realizar o cálculo da equação 3x(a-c)+bxb-4xc através da função resolve_eq , sendo a, b e c os valores de entrada. Ao executar esse programa, é possível perceber que ele apresenta alguns erros. Analise o código e faça os ajustes necessários para que ele funcione corretamente. É necessário realizar mais de uma alteração para que ele funcione de acordo com os exemplos disponibilizados.

def resolve_eq(n1, n2, n3):
  print(3*n1-n3+n2*n2+4*n3)
a, b, c = input().split()
resolve_eq(a, b, c)

A Entrada consiste de:
Três números inteiros a, b e c, separados por espaço.

A Saída deve apresentar:
O resultado da equação realizada pela função resolve_eq .

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Relembre as funções apresentadas no Capítulo 3.

Descrição dos Exemplos:
Os exemplos são autoexplicativos. Dada as entradas basta aplicar na equação.
'''
# Realize as alterações necessárias no código apresentado.
a, b, c = map(int, input().split())


def resolve_eq(n1, n2, n3):
    print(3*(a-c)+(b*b)-(4*c))


resolve_eq(a, b, c)
