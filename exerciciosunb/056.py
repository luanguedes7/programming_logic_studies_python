'''
História de Pescador
Crie um programa que lê strings atribuindo a variável peixe e as armazena na lista rede. As strings devem ser lidas até que seja lido "acabei".

Após isso, deve ser impressa a mensagem: "Hoje eu pesquei:" e os elementos da lista rede, um em cada linha.

Entrada
A entrada contém uma quantidade variável de strings.

Saída
A saída consiste em uma mensagem e os elementos da lista lida.

Observações
No primeiro exemplo de teste, foi digitado "bacalhau" e "acabou", retornando "Hoje eu pesquei: bacalhau".
No segundo exemplo de teste, foi digitado "salmão", "atum" e "acabou", retornando "Hoje eu pesquei: salmão atum".
No terceiro exemplo de teste, foi digitado "nada acabou", retornando "Hoje eu pesquei: nada".
'''
peixes = ''
redes = []

while True: 
    peixes = input()

    if peixes == 'acabou':
        break
    else:
        redes.append(peixes)

print('Hoje eu pesquei:')
for i in redes:
    print(i)

