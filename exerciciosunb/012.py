'''
nvasores Espaciais
Como comandante de uma das naves mais suntuosas e bem equipadas de toda galáxia, é comum que todo tipo de criatura mal intencionada tente se infiltrar em seu veículo. Sua tripulação, no entanto, consiste somente de androides altamente capacitados que lhe custaram uma fortuna. Para economizar, você decidiu programar por si só as funções essenciais de segurança da tripulação.

Elabore duas funções reportar_invasores() e eliminar(). 

A função reportar_invasores() deve receber como parâmetro um número inteiro n e mostrar na tela a mensagem: "Missão, há n invasores às 12 horas!", onde n é o número de invasores que a função recebe como parâmetro.

A função eliminar() recebe como parâmetro um número inteiro n que representa a quantidade de invasores presentes.  Primeiramente, a função deve reportar os n invasores. Em seguida, deve mostrar a mensagem "PEW " n vezes. Por fim, a função deve exibir a mensagem "Alvos eliminados."

A Entrada consiste de:
Não se aplica.

A Saída deve apresentar:
Não se aplica.

Observações:
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado. Para o caso dessa questão é pedido apenas a definição das duas funções e nada mais.
É possível mostrar uma mesma mensagem n vezes usando a função print(). Para isso só é necessário multiplicar a string que se deseja exibir. Por exemplo print("oi "*2) mostraria "oi oi " na tela.

Descrição dos Exemplos:
No primeiro exemplo a função eliminar() recebe como parâmetro o número 1. Conforme descrito, a função chama reportar_invasores() tomando como parâmetro o número 1, que reporta 1 invasor. Em seguida, mostra na tela a mensagem "PEW " uma única vez. Por fim, mostra a mensagem "Alvos eliminados."
No segundo exemplo a função eliminar() recebe como parâmetro o número 3; Conforme descrito, a função chama reportar_invasores() tomando como parâmetro o número 3, que reporta 3 invasores. Em seguida, mostra na tela a mensagem "PEW PEW PEW ". Por fim, mostra a mensagem "Alvos eliminados."
'''
def reportar_invasores(n):
    print(f'Missão, há {n} invasores às 12 horas!')

def eliminar(n):
    pewvezes = 'PEW ' * n
    reportar_invasores(n)
    print(pewvezes)
    print('Alvos eliminados.')

eliminar(1)
eliminar(2)

