'''
Tesouro
Péricles está em uma caverna, onde supostamente existe um tesouro. No entanto está muito escuro na caverna e, portanto, Péricles pediu sua ajuda para saber quantos passos ele tem que andar até o tesouro, se é que existe um. Entretanto, deve-se considerar um problema adicional: partes da caverna colapsaram, então Péricles talvez não consiga chegar até o tesouro, mesmo que ele exista.

O mapa funciona da seguinte maneira: é uma string (a caverna é bem estreita, e só da pra andar para a esquerda ou direita) composta por ' ', '#', 'P' e 'X'. O espaço em branco ' ' indica uma parte intacta da caverna, por onde Péricles pode passar; 'P' é a posição de Péricles; 'X' indica o tesouro; e '#' indica uma parte da caverna colapsada, por onde Péricles não pode passar. 

Entrada

A entrada consiste numa string s, indicando o mapa.

Saída

Imprima "Péricles, não tem tesouro" se não houver tesouro na caverna.

Imprima "Péricles esse caminho não funciona" se não houver um caminho que leve Péricles até o tesouro de sua posição atual.

Imprima "Péricles, d passos", onde d é o número de passos que Péricles precisa andar até o tesouro. Se for para a direita, d será um número positivo. Se for para a esquerda, d será um número negativo.

Observações

No primeiro exemplo, Péricles está a 4 passos de distância do tesouro, e não tem nenhuma parede entre ele e o tesouro, então é possível chegar até lá;
O segundo exemplo é semelhante ao primeiro, mas Péricles tem que se mexer para a esquerda, resultando em −4 passos;
No terceiro exemplo de teste, existem partes da caverna colapsadas entre Péricles e o tesouro, então não é possível chegar até ele.
'''
mapa = '#X   P#'

def existeCaminhoViavel(mapa):
    pos_per = mapa.find('P') #posição do Péricles
    pos_tes = mapa.find('X') #posição do Tesouro
    mapa_fatiado = mapa[int(pos_per): int(pos_tes)+1] 
    print(mapa_fatiado)
    for i in mapa_fatiado:
        if i == '#':
            return False
    return True

def quantidadeDePassos(mapa):
    '''Retorna a quantidade passos que Péricles deve andar'''
    pos_per = mapa.find('P') #posição do Péricles
    pos_tes = mapa.find('X') #posição do Tesouro
    if pos_per > pos_tes:
        mapa = mapa[::-1] #inverter o mapar
        pos_per = mapa.find('P') #posição do Péricles
        pos_tes = mapa.find('X') #posição do Tesouro
        mapa_fatiado = mapa[int(pos_per): int(pos_tes)+1]
        return -(mapa_fatiado.count(' ') +1) 
    
    
    mapa_fatiado = mapa[int(pos_per): int(pos_tes)+1] 
    return mapa_fatiado.count(' ') + 1 # Mais 1, pois indica o passo do Tesouro


if mapa.count('X') == 0:
    print('Péricles, não tem tesouro')
elif existeCaminhoViavel(mapa):
    print(f'Péricles, {quantidadeDePassos(mapa)} passos')
else:
    print('Péricles esse caminho não funciona')
    



