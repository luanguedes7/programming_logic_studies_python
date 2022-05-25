'''
Jovem Físico
Ao entrar em Ciência da Computação, houve um erro na matrícula de Zikarias e ele acabou sendo registrado em um currículo bem antigo que exigia a disciplina Física 1! Que azar. Ele estava completamente perdido no seu primeiro dever de casa e chegou na aula sem entregar nada. Seu professor ficou muito nervoso e decidiu dar uma lição nele. Ele deu uma tarefa que ninguém poderia resolver. Você consegue ajudá-lo?

Você receberá um corpo estacionário no espaço e as forças que o afetam. O corpo estacionário pode ser considerado um ponto material com coordenadas (0, 0, 0). Zikarias só precisa responder se as forças que afetam o corpo estão em equilíbrio. "Fácil", pensou Zikarias, "Só precisamos conferir se a soma de todos os vetores é igual a 0". Só que quando Zikarias foi resolver o problema, ele ficou abarrotado com tantas forças e desistiu, e é aí que você entra. Escreva um programa que determine se um corpo está estacionário ou movendo de acordo com os vetores de forças.

A Entrada consiste de:
A primeira linha contém um inteiro 1≤n≤100 representando o número de vetores.
Depois, há n linhas contendo 3 inteiros cada: as coordenadas xi, yi, e zi do vetor de forças i aplicado ao corpo.

A Saída deve apresentar:
Uma única linha contendo a palavra " YES" (sem aspas duplas) se o corpo está estacionário ou "NO" (sem aspas duplas) caso contrário.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No primeiro exemplo, são solicitados 3 vetores. A soma de todas as coordenadas é igual 6 e, portanto, a resposta é 'NO'.
No segundo exemplo, são solicitados 3 vetores. A soma de todas as coordenadas é igual a 0 e, portanto, a resposta é 'YES'.
'''
n = int(input())
v1 = 0  # variável de controle 1
s1, s2, s3 = 0, 0, 0  # variáveis que correspondem a soma dos vetores em cada eixo
while v1 < n:
    n1, n2, n3 = map(int, input().split())
    # Somando os de cada vetor nos eixos correspondentes
    s1 += n1
    s2 += n2
    s3 += n3
    # Adicionando 1 ao contador/var_controle
    v1 += 1

if s1 ==0  and s2 == 0 and s3 ==0:
    print('YES')
else:
    print('NO')
