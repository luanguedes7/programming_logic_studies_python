'''
Depurando Listas 3.
O uso de listas sem os devidos cuidados (e de outros objetos mutáveis) pode levar a longas horas de depuração. Abaixo um programa em Python que usa listas de forma errada. O seguinte programa deveria ler nomes que estão em uma única linha separados por espaços em branco, armazena-los em uma lista e imprimir os nomes que se repetem em ordem alfabética, colocando a quantidade de vezes que aparecem na lista. Depure o programa para fazê-lo funcionar corretamente.

nomes = input().split()
nomes = nomes.sort()
repetido = 0
temp = ""
saida = []
for i in nomes:
    if i == temp:
        repetido += 1
        mudou = True
    else:
        if mudou:
            saida + [temp, repetido]
            repetido = 0
            mudou = False
    temp = i
for i in saida:
    print(i[0], i[1])
Entrada
Uma linha com diversos nomes separados por espaços em branco.

Saída
Os nomes que aparecem mais de uma vez na linha, um por linha, seguido do número vezes que aparecem na linha.

Observação
Os exemplos são auto-explicativos.
'''
nomes = input().split()
nomes.sort()
repetido = 0
temp = ""
saida = []
#mudou = False não foi necessário

for i in range(len(nomes) -1): #(len(nomes)-1) - evitar erro na última
    temp += nomes[i + 1]
    if nomes[i] == temp or nomes[i] == temp:
        repetido += 1
    
    else:
        saida = saida + [i, repetido]
        repetido = 0
        #mudou = False não foi necessário

for i in range(len(saida) - 1):
    print(saida[i], saida[i+1])