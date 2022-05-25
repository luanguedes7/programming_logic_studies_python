def replace(listaTuplas, elemento):
    novaLista = []

    for i in listaTuplas:
        novaTupla = i[:len(i) - 1] + (elemento,)
        novaLista.append(novaTupla)

    return novaLista

l = [(1, 2, 5, 6, 1), (3, 4, 2), (0, -1, 44)]
x = 99
resposta = replace(l, x)
print(resposta)