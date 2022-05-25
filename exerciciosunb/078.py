linha = int(input())

with open('/etc/passwd/', mode = 'r') as arquivo:

    linhaLidas = arquivo.readlines()
    l = 0

    for i in linhaLidas:
        if linha == l:
            print(i)
            break
        else:
            l += 1
