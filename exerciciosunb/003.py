'''
Dobro Triplo
Elabore um programa que receba duas palavras e retorne a concatenação da primeira repetida duas vezes com a segunda repetida três vezes. 


A Entrada consiste de:
Duas strings, uma em cada linha, conforme os exemplos.

A Saída deve apresentar:
Uma única string no formato especificado no enunciado.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.

Descrição dos Exemplos:
No primeiro exemplo, a saída é "olaolamundomundomundo", uma concatenação de "olaola" ("ola" duas vezes) com "mundomundomundo" ("mundo" três vezes).
No segundo exemplo, a saída é "lalaranjaranjaranja", a string "la" duas vezes e "ranja" três vezes.
'''

string1 = input()
string2 = input()

strings_concatenadas = (2*string1) + (3*string2)

print(strings_concatenadas)