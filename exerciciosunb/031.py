'''
Canetrincas
Felipe, mais conhecido como Font, é apaixonado por canetas. Porém, ele só anda com trincas de canetas de cores diferentes, pois diz a lenda de sua cidade, que quem não segue essa regra, nunca irá casar. Font, por almejar muito encontrar sua pitanguinha, sempre anda com três canetas de cores diferentes. Ele então comprou na internet várias canetas da cor preta, vermelha e azul. Obviamente ele encomendou todas com a mesma quantidade para formar as trincas, porém quando a encomenda chegou, percebeu que elas tinham quantidades diferentes. Font, supersticioso como sempre, decidiu então guardá-las em caixas de forma que houvesse uma quantidade igual de canetas de mesma cor em cada caixa e também essa quantidade fosse a maior possível para todas as três canetas.

Como Font está muito ocupado com suas canetas e tentando conquistar uma gatinha, ele pediu para você implementar uma função calculaCaixa que recebe três inteiros p,v,a correspondendo a quantidade recebida de canetas da cor preta, vermelha e azul e retorne qual a quantidade de caixas ele deve arrumar para guardar suas canetas.

A Entrada consiste de:
Nos parâmetros da função calculaCaixa que são os três números inteiros p, v e a (2≤p,v,a≤10000 ) representando a quantidade de canetas de cada cor que ele recebeu.

A Saída deve retornar:
Um número inteiro correspondendo a quantidade máxima de caixas de forma a atender os requisitos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, o resultado é 4, pois é possível arrumar no máximo quatro caixas em que cada caixa tenha o maior número possível de canetas de mesma cor e todas as caixas tenham quantidades iguais de canetas de cores iguais.
No segundo exemplo, o resultado é 1, pois não é possível usar mais caixas de forma que as propriedades se mantenham.
No terceiro exemplo, o resultado é 10, pois é possível arrumar no máximo dez caixas de forma que todas as canetas de mesma cor tenham sido divididas igualmente entre as caixas e também é o maior valor possível.
'''
'''p = a = v'''
def calculaMDC(n1, n2):
    divisao = n1%n2
    if divisao == 0:
        return n2
    else:
        return calculaMDC(n1 = n2, n2 = n1%n2)

def calculaCaixa(p, v, a):
    valor_max = max(p, v, a)
    valor_min = min(p, v, a)
    
    if valor_min< p < valor_max:
        valor_med = p
    elif valor_min< v < valor_max:
        valor_med = v
    else:
        valor_med = a

    if valor_max % valor_min == 0 and valor_med % valor_min == 0:
        return valor_min            
    elif valor_max %valor_min == valor_med % valor_min:
        return calculaMDC(valor_max, valor_min)
    else:
        return 1