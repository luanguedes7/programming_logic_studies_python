'''
Está dentro?
Construa um programa para verificar, à partir de dois valores A e B, se B corresponde aos últimos dígitos (os menos significativos, mais à direita) de A.

Entrada
A entrada consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 100 dígitos.

Saída
Imprima "ta dentro!!!" se B corresponde aos últimos dígitos de A, e "ta fora..." caso contrário
'''

a, b = input().split()

tamanho_a = len(a)
tamanho_b = len(b)
a_fatiado = a[len(a)-len(b):] #Pegando somente a parte final do a, a partir do tamanho do b

if b in a_fatiado:
    print('ta dentro!!!')
else:
    print('ta fora...')

