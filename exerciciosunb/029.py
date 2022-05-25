'''
Eh divisível?
Crie um programa que lê dois inteiros x e y com y≠0 e chama uma função que verifica se x é divisível por y.

A função retorna True se x for divisível por y e False caso o contrário.

Com o valor retornado da função, imprima "x eh divisivel por y" caso seja True e "x nao eh divisivel por y" caso False.

Entrada
A entrada consiste de dois inteiros positivos.

Saída
A saída será uma das mensagens dependendo do resultado da função.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No primeiro exemplo, 8 é divisível por 2, então a saída será "x eh divisivel por y".
No segundo exemplo, 6 não é divisível por 4, então a saída será "x nao eh divisivel por y".
'''

num1 = int(input())
num2 = int(input())

def ehDivisivel(num1, num2):
    return 'x eh divisivel por y' if num1 % num2 == 0 else 'x nao eh divisivel por y'

print(ehDivisivel(num1, num2))