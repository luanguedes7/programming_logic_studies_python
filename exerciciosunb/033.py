'''
Implicação
É muito comum em programação usarmos operadores lógicos. Python fornece 3 operadores lógicos: not, and e or. Esses três são suficientes para descrever qualquer expressão lógica, mas não são os únicos que existem.

Um outro operador lógico que existe é o condicional. Sejam p e q expressões lógicas, a operação condicional p→q é definida de acordo com a tabela verdade abaixo.

Seu trabalho será implementar a operação lógica condicional, mas para 3 expressões. Para isso, implemente uma função cond, que recebe os argumentos p, q e r (booleanos), e retorne o resultado de p→q→r. Obs.: condicional é uma operação left-associative, ou seja, p→q→r é a mesma coisa que (p→q)→r.

A Entrada consiste de:
Parâmetros da função cond que são os booleanos p, q e r.

A Saída deve apresentar:
Sua função deve retornar um booleano, que é o resultado de p→q→r.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, a primeira implicação diz que 1 ser menor do que 2 implica que 1 é menor do que 3 (obviamente verdade), e isso implica que 1 é menor do que 5 (também verdade).
No segundo exemplo, a primeira implicação diz que 1 ser menor do que 2 implica que 1 é menor do que 3 (obviamente verdade), e isso implica que 1 é maior que 5, o que é falso.
'''


def cond(p, q, r):
    pq = 'None'

    if p == q or (p == False and q == True and p != q):
             pq = True
    else:
             pq = False

    return True if pq == r or (pq == False and r == True and pq != r) else False

 
print(cond(0 == 0, 0 < 0, 1> 0))

