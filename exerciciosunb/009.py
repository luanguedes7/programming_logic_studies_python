'''
Len_str
Crie a função len_str que recebe uma string s como argumento. Imprima n vezes a string s em que n é o tamanho da string. Observe nos exemplos os casos de saída.

A Entrada consiste de:
Parâmetros da função len_str, que é uma string s como descrito no enunciado.

A Saída deve apresentar:
n vezes a string s

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, a string "oi" tem 2 caracteres e portanto ela foi repetida 2 vezes: "oioi".
No segundo exemplo, a string "UNB" tem 3 caracteres e portanto ela foi repetida 3 vezes: "oioi"
'''
string = 'oioi'
tamanho_string = len(string)
string_multiplicada = string * tamanho_string


def len_str():
    print(string_multiplicada)

len_str()

#TypeError: len_str() takes 0 positional arguments but 1 was given
#staticmethod and self
#saindo oioi na linha de baixo, estranhamente. Usei o end = ''
