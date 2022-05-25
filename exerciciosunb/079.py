prato = input()
cardapio = []
preco = []
pagamentos = []

with open('cardapio.txt', mode = 'r') as arquivo:
    cardapioL = arquivo.readlines()

    for l in cardapioL:

        if prato.title() in l or prato in l:

            l = l.split(sep = '/')
            a = l[1].replace('\n', '')
            c = f"{l[0]} {a}"
            cardapio.append(c)

            p = float(l[1].replace('\n', ''))
            preco.append(p)

with open('carteira.txt', mode = 'r') as arquivo:
    carteiraL = arquivo.readlines()

    for l1 in carteiraL:
        
        l1 = l1.split(sep = '/')
        p1 = float(l1[1].replace('\n', ''))
        pagamentos.append(p1)

if len(cardapio) > 0:
    for i in cardapio:
        print(i)

    precoT = sum(preco)

    if precoT <= float(pagamentos[0]):
        print(f'Sua conta deu: {precoT:.2f}')
        print('Vou pagar com dinheiro')

    elif precoT <= float(pagamentos[1]):
        print(f'Sua conta deu: {precoT:.2f}')
        print('O jeito é pagar com o cartão de crédito')
    else:
        print(f'Sua conta deu: {precoT:.2f}')
        print('Ah não! Vou ter que lavar prato!')
else:
    print('Infelizmente não temos este prato')