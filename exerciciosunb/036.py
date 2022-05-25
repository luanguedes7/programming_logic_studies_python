'''
Cerveja Pong
Ontem mesmo o prof Faina encontrou com o prof Emidio (de forma virtual) e tiveram uma conversa legal sobre a Cerveja Pong. Daí ele se perguntou, será que o ano em que o prof Emidio nasceu é primo?

Entrada
A única linha de entrada contém um inteiro  1≤n≤105 que representa o ano em que Emidio nasceu. Não é necessário validar se os números estão dentro do intervalo definido.

Saída
Imprima "Emidio" se o ano em que Emidio nasceu é primo e "Faina" caso contrário.

Observações

No primeiro caso de teste, o resultado é "Emídio" pois o número 2 é um número primo.
No segundo caso de teste, o resultado é "Emídio" pois o número 3 é um número primo.
No terceiro caso de teste, o resultado é "Faina" pois o número 4 não é um número primo.
'''
numero_entrada = int(input())
numero_da_divisao = 1
quantos_divisores = 0
resto_divisao = 0

while numero_da_divisao <= numero_entrada:
    resto_divisao = numero_entrada % numero_da_divisao
        
    if resto_divisao == 0:
        quantos_divisores += 1 
    
    numero_da_divisao += 1

if quantos_divisores == 2:
    print('Emídio')
else:
    print('Faina')





    