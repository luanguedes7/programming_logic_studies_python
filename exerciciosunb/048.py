'''O Valor das Palavras
Um padrão comum de codificação de caracteres é ASCII - confira a tabela ascii aqui. Esse código atribui um valor de 0 até 127 para alguns caracteres comuns, por exemplo o valor ascii para 'A' é 65.

Dado uma string s diga qual o valor total da string, definido como a soma do valor de cada caractere.

Entrada

A entrada consiste em uma string s (0≤|s|≤104 ). s é composta por letras, números e símbolos de pontuação.  

Saída

Imprima o valor de s, definido como a soma dos valores de cada caractere no código ASCII. 

Observações

No primeiro exemplo de teste, s=abc. Olhando na tabela, a=97;b=98;c=99, então somamos os valores 97+98+99=294, que é a resposta.
'''

string = input()
soma_da_string = 0 # valor de cada caracter da string somado segundo a ASCII
for letter in string:
    letter = ord(letter) #função que retona o valor do caractere na tabela ASCII
    soma_da_string += letter

print(soma_da_string)
