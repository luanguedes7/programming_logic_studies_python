n1, n2 = map(int, input().split())
s_entre_c = 0 #espaços entre as cadeiras
l_c_e_c = [] #lista com espaços entre as cadeiras

for i in range(n1):
    lista = list(map(int, input().split()))
    s_entre_c = 0

    for j in range(len(lista) - 1):
        if lista[0] == 0 or lista[len(lista) - 1] == 0:
            if lista[j] == 0:
                s_entre_c += 1
            else:
                if s_entre_c != 0:
                    l_c_e_c.append(s_entre_c)
                    s_entre_c = 0
        else:
             if lista[j] == 0:
                s_entre_c += 1
             else:
                 if s_entre_c != 0:
                    l_c_e_c.append(s_entre_c - 1)
                    s_entre_c = 0
        
        

l_c_e_c.sort()

maior_espaco = l_c_e_c[len(l_c_e_c) - 1:len(l_c_e_c)]

print(*maior_espaco)


    
