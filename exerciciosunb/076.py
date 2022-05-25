genero = input()
genero = genero.title()
duracao = int(input()) 
listaDeFilmes = []

with open('filmes.txt', mode = 'r') as arquivo:
    arquivoLido = arquivo.readlines()

    for i in arquivoLido:
        sEmL = i.split(sep='/')
        sEmL[2] = int(sEmL[2].replace('\n', ''))
            
        if sEmL[1] == genero and sEmL[2] <= duracao:
            listaDeFilmes.append(sEmL[0])
    
if len(listaDeFilmes) == 0:
    print('Não foram encontrados filmes assim')
else:
    for i in listaDeFilmes:
        print(i)