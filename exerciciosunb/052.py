'''Strings iguais
Dadas 2 strings a e b, você pode realizar 2 operações com elas:

1. Remover o primeiro caractere da string.

2. Remover o último caractere da string. 

Repare que é possível que a string fique sem caracteres após alguma dessas operações.

Mostre o menor número de operações necessárias para deixar as duas strings iguais.

Entrada

A entrada consiste em 2 strings a e b, 1≤|a|,|b|≤50. 

Saída

O menor número de operações necessárias para deixar as duas strings iguais.

Observações

No primeiro exemplo as duas strings já são iguais, então precisamos de 0 operações.
No segundo exemplo temos que remover "ab" da primeira string. Independente se remover o primeiro ou o segundo "ab", são 2 operações.
No terceiro exemplo realizamos 3 operações na primeira string e 1 na segunda. Dessa forma as duas se tornam a string vazia, e portanto iguais.
'''

string1 = input()
string2 = input()
numero_de_operacoes = 0
p = 1


while True:
    if string1 == string2:
        break
    else:
        if string2 in string1:
            pos2em1 = string1.find(string2)
            
            if pos2em1 > 0:  
                string1 = string1[p:]
                numero_de_operacoes += 1
            else:
                n = len(string1) - 1
                string1 = string1[0:n]
                numero_de_operacoes += 1
        elif string1 in string2:
            pos1em2 = string2.find(string1)
            
            if pos1em2 > 0:  
                string2 = string2[p:]
                numero_de_operacoes += 1
            else:
                n = len(string2) - 1
                string2 = string2[0:n]
                numero_de_operacoes += 1
        else:
            n = len(string1) - 1
            m = len(string2) - 1
            string1 = string1[0:n]
            string2 = string2[0:m]
            numero_de_operacoes += 2

print(numero_de_operacoes)



