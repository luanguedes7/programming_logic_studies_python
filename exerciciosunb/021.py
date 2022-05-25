'''
Desconto
Na loja de Laiane o parcelamento funciona de uma maneira diferente: o valor da parcela não possui centavos, assim como o valor de qualquer produto dessa loja. Sendo assim, se a compra ficou em 355 reais e esta for parcelada em quatro vezes, as parcelas serão de 88 reais e o restante do valor deve ser pago no ato da compra, ou seja, o cliente pagará à vista 3 reais e dividirá 352 reais em quatro vezes de 88 reais. Todavia, para um cliente afiliado o que ocorre é que ele não precisa pagar o resto, isto é, ele faz uma compra de 355 reais, parcela em 4 vezes e tem um desconto de 3 reais, pagando apenas 352.

Laiane resolveu que essa semana dará esse desconto para qualquer cliente, sendo filiado ou não, nas compras a partir de 350 reais.

Escreva um programa que dado o valor da compra, o número de parcelas e uma flag que indica se o cliente é afiliado ou não (0 - não afiliado, 1 - afiliado) retorne: "Por favor, pague x reais para prosseguir com o parcelamento" para os clientes não afiliados (onde x é a quantia em reais que o cliente deve pagar no ato da compra) ou "Eba! Você ganhou x reais de desconto!" para um cliente afiliado, ou para qualquer cliente que tenha comprado a partir de 350 reais.

A Entrada consiste de:
Três números inteiros positivos, todos na mesma linha: valor do produto, número de parcelas (sempre maior que um) e uma flag (0 ou 1) para saber o tipo de cliente.

A Saída deve apresentar:
Uma string, como ilustra os exemplos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No primeiro exemplo, a compra foi de 200 reais, o número de parcelas é 3 e é um cliente afiliado. Logo serão três parcelas de 66 reais , totalizando 198 reais com um desconto de 2 reais.
No segundo exemplo, o valor da compra é 416 reais dividido em 4 parcelas. Uma vez que a compra foi superior a 350 reais, mesmo não sendo um cliente afiliado, houve um desconto de 1 real (cinco parcelas de 83 reais).
'''


def parcelamento_loja(n1, n2, n3):
    '''n1 = valor do produto, n2 = número de parcelas(>1), n3 = flag(0, 1)'''
    cliente_afiliado = True
    desconto = n1 % n2
    valor_a_vista = n1 % n2

    if n3 == 0:
        cliente_afiliado = False

    if cliente_afiliado or n1 > 350:
        print(f'Eba! Você ganhou {desconto} reais de desconto!')
    else:
        print(
            f'Por favor, pague {valor_a_vista} reais para prosseguir com o parcelamento')
