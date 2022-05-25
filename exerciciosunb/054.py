'''
Corretor
Luca está ajudando seu irmão mais novo Maurinho a escrever algumas frases. Como seu irmão está em fase de alfabetização, às vezes ele confunde algumas letras com algarismos e escreve a frase de maneira incorreta. Pela similaridade, o irmão pode fazer as seguintes confusões:

p --> 9

b --> 6

s --> 5

t --> 7

o --> 0

i --> 1

Além disso, algumas frases de Maurinho estão sem ponto final e o início da frase não apresenta letra maiúscula, podendo algumas letras estarem maiúsculas em partes inapropriadas da frase.  Ajude Luca a ajudar o irmão, escrevendo um programa que recebe uma frase e a corrige. A frase correta é aquela sem números, com a ocorrência de letra maiúscula apenas no início da frase e que possui ponto final.

A Entrada consiste de:
Uma string representando a frase de Maurinho.

A Saída deve apresentar:
Uma string representando a frase corrigida.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
'''

frase = input()

for letra in frase:
    if letra == '9':
        frase = frase.replace('9','p')
    elif letra == '6':
        frase = frase.replace('6','b')
    elif letra == '5':
        frase = frase.replace('5','s')
    elif letra == '7':
        frase = frase.replace('7', 't')
    elif letra == '0':
        frase = frase.replace('0','o')
    else:
        frase = frase.replace('1','i')

frase = frase.capitalize()
ultimo_caracter = frase[len(frase) -1 :len(frase)]
if ultimo_caracter == '.':
    print(frase)
else:
    print(frase + '.')