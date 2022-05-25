'''
Irmão mais velho
A família Cacãope está em crise. Eles não sabem qual dos dois filhos é o mais velho! Por sorte, encontraram você, um primo distante para ajudá-los.

Escreva uma função chamada older(ageA, ageB) que receberá a idade em anos completos dos filhos A e B e deverá imprimir A se o filho A for com certeza mais velho, B se o filho B for com certeza mais velho e Maybe twins se não for possível saber com certeza quem é o mais velho.


A Entrada consiste de:
Dois inteiros ageA,ageB que indicam a idade em anos completos dos filhos A e B, respectivamente.

A Saída deve apresentar:
A se o filho A for com certeza mais velho, B se o filho B for com certeza mais velho e Maybe twins se não for possível saber com certeza quem é o mais velho.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, o filho A tem 5 anos e o filho B tem 10 anos, então B é o filho mais velho.
No segundo exemplo, o filho A tem 19 anos e o filho B tem 17 anos, então A é o filho mais velho.
'''
def older(ageA, ageB):
    older = 'None'
    if ageA > ageB:
        older = 'A'
    elif ageA < ageB:
        older = 'B'
    else:
        older = 'Maybe twins'

    print(older)