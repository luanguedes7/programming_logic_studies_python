numGatos = int(input())
bilhetePremiado = input()
gatosBilhetes = dict()

for i in range(numGatos):
    gato, bilhete =  input().split('-', maxsplit= 1)

    gatosBilhetes[bilhete] = gato


if bilhetePremiado in gatosBilhetes:
    print('deu bom!')
    print(gatosBilhetes.get(bilhetePremiado, 0))
else:
    print('não foi dessa vez /:')
