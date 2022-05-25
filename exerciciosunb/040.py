'''
N+1 elefantes incomodam muito mais!
Um elefante incomoda muita gente, dois elefantes incomodam, incomodam muito mais... n+1 elefantes incomodariam quanto mais?
Implemente um programa que recebe a quantidade de elefantes e escreva a letra da música.

A Entrada consiste de:
Um número inteiro positivo 0<n≤500 indicando a quantidade de elefantes.

A Saída deve apresentar:
O refrão da música para a quantidade de elefantes dada, começando com 1 e incrementando até que se saiba dos n+1 elefantes. Apresente uma frase por linha.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No terceiro exemplo, existem 3 elefantes. Então é impresso que 1 elefante incomoda muita gente e que 2 elefantes incomodam incomodam muito mais. Na sequência inicia-se uma repetição informando que: 2 elefantes incomodam muito gente e 3 elefantes incomodam, incomodam, incomodam muito mais; e que 3 elefantes incomodam muita gente e 4 elefantes incomodam, incomodam, incomodam, incomodam muito mais.
'''
n_elefantes = int(input())

n = 1

while n <= n_elefantes:
    span_incomoda = (n) * "incomodam, "
    if n == 1:
       frase1 = f'{n} elefante incomoda muita gente...'
       frase2 = f'{n+1} elefantes {span_incomoda}'
       print(frase1)
       print(frase2 + 'incomodam muito mais...')
    else:
       frase3 = f'{n} elefantes incomodam muita gente...'
       frase4 = f'{n+1} elefantes {span_incomoda}'
       print(frase3)
       print(frase4 + 'incomodam muito mais...')
    n += 1