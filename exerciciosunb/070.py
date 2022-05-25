def stockmarket(stock):
    saida = dict()

    for i in stock:
        if i[0] in saida:
            valorAdicional = i[1] * i[2]
            saida[i[0]] += float(valorAdicional)
        else:
            saida[i[0]] = float(i[1] * i[2])

    return saida

	
