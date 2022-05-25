p, c, a = input().split()
c = int(c)
nRArq = []

with open(a, mode = 'r') as arq:
    rArq = arq.readlines()

    for i in rArq: #Tirar o \n ao final das strings
        i1 = i.replace('\n', '')
        nRArq.append(i1)

    for l in nRArq:
        if p in l:
            indP = nRArq.index(l)
            print(f'{a}: {indP + 1}')

            ii, fi = indP - c, indP
            if not ii < 0:   
                for i in range(ii, indP):
                    print(nRArq[i])
            
            print(nRArq[indP])
            
            for i in range(indP + 1, indP + 1 + c):
                print(nRArq[i])
        
        print()