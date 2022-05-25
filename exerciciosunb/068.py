guicionario = dict()

for i in range(int(input())):
    palavragui, traducao = input().split(maxsplit= 2)

    guicionario[palavragui] = traducao

impressao = input().split()

for i in impressao:
    print(guicionario[i], end =' ')