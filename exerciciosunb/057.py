'''
Substituindo Pares
Crie um programa que lê 10 números inteiros maiores que 0 e os armazena em uma lista numeros. Em seguida, substitua todos os números pares pelo número 1. Por fim, imprima a lista com os números ímpares restantes.

Entrada
A entrada consiste em números inteiros maiores que 0.

Saída
A saída consiste na lista resultante sem números pares.

Observações
No primeiro exemplo de teste, foi digitado 1, 2, 3, 4, 5, 6, 7, 8, 9 e 10, retornando [1, 1, 3, 1, 5, 1, 7, 1, 9, 1].
No segundo exemplo de teste, foi digitado 50, 40, 30, 10, 12, 2, 4, 6, 2 e 54 retornando [1, 1, 1, 1, 1, 1, 1, 1, 1, 1].
No terceiro exemplo de teste, foi digitado 1, 1, 1, 1, 1, 1, 1, 1, 1 e 1, retornando [1, 1, 1, 1, 1, 1, 1, 1, 1, 1].
Não é necessário validar se os valores de entrada estão dentro do intervalo definido.
'''
nums = ''
numeros = []
for i in range(1,10):
    nums = int(input())
    if nums%2 == 0:
        nums = 1

    numeros.append(nums)

    