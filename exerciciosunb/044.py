'''
Vanessa e o ano bonito
Um dia, Vanessa estava lendo jornal quando leu uma curiosidade: após 1987, o ano de 2013 é o primeiro a ter apenas dígitos distintos. A partir desse momento, Vanessa passou a considerar isso um ano bonito. Quando isso aconteceu, Vanessa vivia no ano x, e se perguntou, qual é o próximo ano bonito?

A Entrada consiste de:
De um número inteiro tal que 0≤x≤9999. O ano em que Vanessa se encontra.

A Saída deve apresentar:
Um único inteiro: a resposta do problema.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No primeiro exemplo, o próximo ano bonito em relação a x=1987 é 2013, pois 2013 é o menor número maior do que 1987 em que todos os seus dígitos são distintos. Observe que na sequência de anos após 1987, dada pelos anos 1988,1989,1990,1991,1992,1993,…2011,2012 sempre encontramos algum dígito repetido no ano.
No segundo exemplo, o próximo ano bonito para a entrada x=444 é 450, pois conforme a sequência de anos 445,446,447,448,449…450, o ano 450 possui todos os seus dígitos distintos.
'''
ano = int(input())
ano = ano + 1
ano_controle = ano

while ano_controle != 0:
    ultimo_digito = ano_controle % 10
    zerar_ultimo = ano_controle // 10
    ultimo_digito_zerar_ultimo = zerar_ultimo  % 10

    if ultimo_digito == ultimo_digito_zerar_ultimo:
        ano += 1
        ano_controle += 1
    else: 
        ano_controle = ano_controle // 10
        
print(ano)