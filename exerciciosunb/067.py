def historiagrama(string):
    saida = dict()

    for i in string:
        saida[i] = int(string.count(i))
    
    print(saida)


historiagrama(input())
