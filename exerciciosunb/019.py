'''
Área de Figuras Planas II
Implemente uma função chamada area que imprime a área de uma determina figura geométrica. A função deve receber 3 parâmetros, sendo dois deles valores numéricos e uma string representando a forma geométrica. A área da figura deve ser do tipo inteiro. As formas geométricas permitidas são "retangulo", "losango" e "triangulo".


A Entrada consiste de:
Os parâmetros da função são dois inteiros arg1,arg2≥1 e uma string forma. Em caso de retângulo ou triângulo, os argumentos representam a base e a altura da forma e caso a figura seja um losango, os argumentos representam o valor das duas diagonais.

A Saída deve apresentar:
A frase "O forma tem area de area", conforme os exemplos. Obs.: forma é a string inserida, que pode tomar o nome de quatro formas geométricas: retangulo,losango e triangulo e area é somente o valor inteiro do cálculo da área da forma geométrica dada na string forma, com arg1,arg2 assumindo as incógnitas de cada cálculo de área.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, como a forma é de um losango, foi aplicado a equação que calcula a área do losango dadas as duas diagonais que gerou o resultado 10 computado na frase de saída.
'''
def area(arg1, arg2, forma):
    if forma == 'retangulo':
        '''arg1 = base arg2 = altura '''
        area = int(arg1 * arg2)
    elif forma == 'triangulo':
        '''arg1 = base arg2 = altura'''
        area = int(arg1 * arg2 / 2)
    else:
        '''arg1 e arg2 = diagonais'''
        area = int(arg1 * arg2 / 2)

    print(f'O {forma} tem {area} de area')

area(10, 2, 'losango')
area(20, 4, 'retangulo')
area(15, 3 , 'triangulo')