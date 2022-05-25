'''
Ponto flutuante
Elabore um programa que receba um valor do tipo float e imprima três informações.


A Entrada consiste de:
Um valor do tipo float.

A Saída deve apresentar:
Três linhas, cada uma contendo o valor com 4 casas decimais, depois com 2 casas decimais e por fim, o valor com 0 casas decimais. Veja os exemplos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No segundo exemplo, o valor de entrada é 2.276. Portanto a primeira resposta com 4 casas decimais é 2.2760. A segunda com 2 casas decimais é 2.28. E a terceira é com nenhuma cada decimal é 2.
'''

floatnumber = float(input())

print(f'{floatnumber:.4f}')
print(f'{floatnumber:.2f}')
print(f'{floatnumber:.0f}')