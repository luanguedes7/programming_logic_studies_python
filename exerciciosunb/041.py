'''
Reciclagem
Dan está aprendendo sobre os 3 R's no seu colégio, Reduzir Reutilizar e Reciclar! Ele não conhecia muito sobre ecologia e as aulas ajudaram bastante. Ele está tentando melhorar seus hábitos ecológicos, pois ele quer que seus descendentes tenham um lugar ótimo para viver. Ele já está mudando seus hábitos, utilizar menos fontes fósseis, andar mais de bicicleta, usar menos plástico, usar mais fontes de energia renováveis, (acompanhar a Greta ?) etc. Uma das coisas que ele está melhorando é a reciclagem de papel, para cada 2 papéis reciclados, ele consegue produzir mais 1 papel. Ele quer saber quantos papéis ele terá ao final, se ele tiver no início n papéis.

A Entrada consiste de:
Dois números inteiros n (4≤n≤100000), como descritos no enunciado.

A Saída deve apresentar:
A quantidade total de papéis que ele consegue se reciclar o máximo número de papéis.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No primeiro exemplo, o resultado é 7 pois ele tem 4 papéis, consegue reciclar 2, adicionando na resposta mais dois e com esses dois reciclados consegue reciclar mais um papel, totalizando 7.
No primeiro caso de teste,
'''
n_papeis = int(input())
papeis_prod = 0 # reciclados/2
reciclados = 0
prod_rec = 0 
papeis_tot = n_papeis # + recliclados + produzidos

while True:
    if n_papeis <= 2:
        break
    elif n_papeis % 2 == 0:
        reciclados += n_papeis/2
        papeis_prod +=  reciclados/2
        prod_rec = reciclados + papeis_prod
        n_papeis = n_papeis/2
    else: 
        reciclados += (n_papeis - 1)/2
        papeis_prod +=  reciclados/2
        prod_rec = (reciclados + papeis_prod) + 1 # 1 = papel tirado no início do else
        n_papeis = (n_papeis - 1)/2 

print(f'{int(papeis_tot + prod_rec)}')


