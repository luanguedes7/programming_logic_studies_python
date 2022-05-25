'''Consultas de intervalo na string 2
Guilherme está entediado nessa quarentena e começa a brincar com a criação de substrings, de tamanhos variados, a partir de uma string inicial. Sabendo disso, você entra em contato com Guilherme e faz q consultas sobre possíveis substrings que podem ser geradas. Cada consulta contém dois números inteiros l e r e uma string s=s0s1…sn−1, em que 0≤l≤r<n e si é um caractere alfanumérico. Para responder cada consulta, Guilherme deve gerar uma substring cujos caracteres estejam no intervalo [l,r] da string s, isto é, slsl+1…sr−1sr.

Sua tarefa consiste em gerar a resposta do Guilherme para cada consulta.

Entrada
A primeira linha da entrada contém um número inteiro q (1≤q≤100), indicando a quantidade de consultas. As próximas q linhas descrevem todas essas consultas. Cada consulta é composta por dois números inteiros l e r,  e por uma string s, nessa ordem e separados por espaço em branco. A string s=s0s1…sn−1, em que 1≤n≤100, possui apenas caracteres alfanuméricos, e 0≤l≤r<n.

Saída
Para cada consulta, imprima uma única linha - a substring resultante slsl+1…sr+1sr.

Observações:
Não é necessário verificar se as relações entre l, r e n estão corretas. Assuma que o usuário digitou valores válidos.
No primeiro caso de teste, devem ser realizadas duas consultas. Na primeira são selecionados os caracteres da posição 0 a posição 7 da string apresentada, que gera como resultado a sub-string Atletico. Na segunda consulta são selecionados os caracteres da posição 9 a 18 da string apresentada, que gera como resultado a sub-string Paranaense.
'''

quantidade_consultas = int(input())
z = 0  # variável auxiliar para o while
substring = '' #substring a ser gerada como saída para cada consulta

while z < quantidade_consultas:
    n, m, string = input().split()  # n: indice inicial, m: indice final

    substring = string[int(n):int(m)+1]
    print(substring)
    z += 1
