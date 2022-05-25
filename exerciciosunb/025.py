'''
Calcule as médias
Escreva um programa que leia 3 números inteiros positivos e efetue o cálculo das médias Aritmética (A), Ponderada (P) e Harmônica (H) dependendo da letra dada pelo usuário, mostre qual o tipo de média e qual o valor da média. No caso do usuário digitar qualquer outro caractere, apresente a mensagem 'Operacao inexistente'.

A Entrada consiste de:
Linha contendo as três notas que são três números reais positivos.
Linha contendo um caractere (para determinar qual a média), sendo (P) Ponderada, (H) Harmônica e (A) Aritmética
Caso o caractere seja 'P', deve-se solicitar os três pesos de cada nota enviada, que são números positivos inteiros.

A Saída deve apresentar:
Na primeira linha, o tipo de média que ele fez ("Harmonica", "Ponderada", "Aritmetica" ou "Operacao inexistente")
Na segunda linha, caso tenha sido digito um caractere válido, o resultado da média com precisão de 2 casas decimais.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
Os exemplos são autoexplicativos.
'''
nota1, nota2, nota3 = map(int, input().split())
tipodemedia = input()
if tipodemedia == 'P':
    peso1, peso2, peso3 = map(int, input().split())

if tipodemedia == 'A':
    media = (nota1 + nota2 + nota3) / 3
    print('Aritmetica')
    print(f'{media:.2f}')
elif tipodemedia == 'P':
    media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
    print('Ponderada')
    print(f'{media:.2f}')
elif tipodemedia == 'H':
    media = 3/ (1/nota1 + 1/nota2 + 1/nota3)
    print('Harmonica')
    print(f'{media:.2f}')
else:
    print('Operacao inexistente')