'''
42
A resposta de tudo. Mas qual a pergunta? Bom nesse caso a pergunta é se a soma de algum par de números em um vetor resulta em 42... e a resposta é sim ou não.

Entrada

A entrada consiste em 2 linhas. A primeira contém um inteiro n (1≤1000)

A segunda linha contém n inteiros separados por espaço. Esses números não estão ordenados.

Saída

Imprima "sim"  (sem aspas duplas) caso exista algum par de números cuja soma é 42. Imprima "nao" (sem aspas duplas) caso contrário.

Observações

No primeiro caso de teste, temos os números 20 e 22, cuja soma é 42, então imprimimos sim.
No segundo caso de teste, não existe nenhum par de números cuja soma é 42, então o resultado é nao.
'''
n_elementos = int(input())
lista_ns = list(map(int, input().split()))
s_igual_42 = False
nova_lista_ns = []
lista_ns.sort()

for i in lista_ns:
    if i < 42:
        nova_lista_ns.append(i)

for i in range(len(nova_lista_ns) - 1):
    if nova_lista_ns[i] + nova_lista_ns[i + 1] == 42:
        s_igual_42 = True
        break
    elif  nova_lista_ns[i] + nova_lista_ns[i - 1] == 42:
        s_igual_42 = True
        break


if s_igual_42:
    print('sim')
else:
    print('nao')


