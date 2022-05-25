'''
Operações com strings
Faça um programa que leia duas strings e um número inteiro, e faça as operações de (1) concatenação das duas strings, (2) repetição da primeira string pelo número inteiro de vezes, e (3) ambas operações juntas. A função concatenar deve receber como parâmetro as duas strings e apresentar as duas strings concatenadas. A função repetir deve receber a primeira string e o número inteiro de repetições e apresentar a string repetida pelo número de repetições. Por fim, a função ambos deve receber as duas strings e o número inteiro de repetições e então ela deve concatenar as duas strings e apresentar o resultado repetidas vezes pelo número de repetições.

A Entrada consiste de:
Duas strings e um número inteiro positivo separados por espaço str1,str2,a |a>0.

A Saída deve apresentar:
3 linhas, cada uma como apresentada a seguir.
A concatenação da primeira string com a segunda;
A repetição da primeira string com o número inteiro;
A repetição da string resultante da concatenação da primeira string com a segunda pelo número inteiro de vezes, conforme os exemplos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
'''

s1, s2, n = input().split()
n = int(n)


def concatenar(s1, s2):
    return s1 + s2


def repetir(s1, n):
    return s1 * n


def ambos(s1, s2, n):
    s_concatenada = concatenar(s1, s2)
    s_concatenada_n_vezes = repetir(s_concatenada, n)
    print(s_concatenada_n_vezes)


print(concatenar(s1, s2))
print(repetir(s1, n))
ambos(s1, s2, n)
