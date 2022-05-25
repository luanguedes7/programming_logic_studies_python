'''
Ta ai?
Implemente 3 funções sendo que a primeira se chamará taAi e receberá como parâmetro um valor booleano. Se o valor for True, a função deve chamar outra função to que não recebe nenhum parâmetro e retornar a string "to aqui, chefe". Se o valor for False a função taAi deve chamar a função toNao que não recebe nenhum parâmetro e retorna a string "fui nanar".

A Entrada consiste de:
Os parâmetros da função taAi que é um valor booleando True ou False.

A Saída deve retornar:
A string de acordo com o que foi pedido.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, o resultado é "fui nanar" pois o parâmetro é False.
'''
def to():
    return 'to aqui, chefe'

def toNao():
    return 'fui nanar'


def taAi(a_bool):
    if a_bool:
        to_ai = to()
    else:
        to_ai =toNao()

    return to_ai

    

    
