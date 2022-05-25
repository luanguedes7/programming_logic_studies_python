'''
Triângulo Retângulo
Crie uma função chamada triangulo que recebe como parâmetro dois números reais positivos b e h e retorna a área de um triângulo retângulo de base b e altura h.

A Entrada consiste de:
Não se aplica.

A Saída deve apresentar:
A área do triângulo retângulo.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, a base e altura passados como parâmetro são 3.0 e 4.0 e a área do triângulo, portanto, é 6.0.
'''
n1 = float(input())
n2 = float(input())

def triangulo(b, h):
    area_triangulo = (b * h) / 2
    print(area_triangulo)

triangulo(n1, n2)


