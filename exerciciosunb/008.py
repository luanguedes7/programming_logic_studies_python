'''
Mônica em: criando sequências
Quando está no tédio, Mônica gosta de criar sequências de letras. Mas ela não faz isso de uma maneira aleatória, segue todo um raciocínio para inventar uma sequência e em seguida, ela a escreve em seu caderninho vermelho. 

A fórmula de Mônica para criar uma sequência consiste em alguns elementos: três números inteiros a, b e c, todos maiores que zero e duas sequências p1 e p2 que já existem (podendo ou não ser de autoria da Mônica). Com todos os elementos, a Mônica cria a sequência da seguinte maneira:

Repete a sequência "p1" a+b vezes;
 Repete a sequência "p2" b+c vezes;
Concatena o resultado do primeiro passo com o resultado do segundo passo;
Repete o resultado do terceiro passo a+c vezes.
Mônica gostaria de automatizar esse processo elaborando um programa com toda a lógica que ela desenvolveu, mas como o PC dela foi pro conserto, ela não pode fazer. Você poderia fazer esse favor a ela? 


A Entrada consiste de:
Três números inteiros positivos.
Duas strings, uma em cada linha, como apresentado nos exemplos.

A Saída deve apresentar:
Uma string, representando a sequência criada por Mônica.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Se atente aos parênteses.
'''

a = int(input())
b = int(input())
c = int(input())
p1 = input()
p2 = input()

passo1 = (a+b)*p1
passo2 = (b+c)*p2
passo3 = passo1 + passo2
passo4 = (a+c)*passo3

print(passo4)
