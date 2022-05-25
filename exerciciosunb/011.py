'''
Como separa?
A biblioteca do Python oferece módulos embutidos que fornecem acesso à funcionalidades do sistema e também módulos que fornecem soluções padronizadas para muitos problemas que ocorrem em programação cotidiana.

Analisando o código abaixo, qual o valor da variável separador para que cada uma das quatro palavras de uma lista de 4 palavras, sejam atribuídas as variáveis palavra1, palavra2, palavra3 e palavra4.

frase_lista = input()
separador = "?"
palavra1, palavra2, palavra3, palavra4 = frase_lista.split(separador)
print(f'#{palavra1}#')
print(f'#{palavra2}#')
print(f'#{palavra3}#')
print(f'#{palavra4}#')
'''

frase_lista = "maçã, banana, melancia, limão"
separador = ", "
palavra1, palavra2, palavra3, palavra4 = frase_lista.split(separador)
print(f'{palavra1}')
print(f'{palavra2}')
print(f'{palavra3}')
print(f'{palavra4}')
