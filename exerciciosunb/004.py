'''
3 Caracteres
Elabore um programa que leia 3 caracteres do teclado e apresente-o de diversas formas diferentes, de acordo com o solicitado.

Os caracteres lidos, juntos;
Somente o primeiro caractere lido;
Duas vezes o segundo caractere lido;
Três vezes o terceiro caractere, separados por um espaço;
A mensagem "X == x, Y == y, Z == z" (onde x, y e z devem ser substituídos pelos caracteres lidos);
A mensagem "X != y, Y != x, Z == z" (onde y, x e z devem ser substituídos pelos caracteres lidos).

A Entrada consiste de:
três caracteres x,y e z alfanuméricos (uma letra do alfabeto latino, maiúscula ou minúscula, ou um dígito), um por linha.

A Saída deve apresentar:
6 linhas, cada uma contendo as respostas aos itens solicitados, conforme apresentado nos exemplos.

Observações:
Não é necessário validar se os valores de entrada são do tipo definido.

Descrição dos Exemplos:
No primeiro exemplo, as letras a, b e c são a entrada e as saídas são apresentadas 1 em cada linha, relativas ao que foi solicitado nos itens 1 a 6 do enunciado.
'''

x = input()
y = input()
z = input()

formaum = x+y+z
formadois = x
formatres = 2 * y
formaquatro = z + ' ' + z + ' ' + z
formacinco = f'X == {x}, Y == {y}, Z == {z}'
formaseis = f'X != {y}, Y != {x}, Z == {z}'

print(formaum)
print(formadois)
print(formatres)
print(formaquatro)
print(formacinco)
print(formaseis)

