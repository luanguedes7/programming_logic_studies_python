'''
Será que é potência
Dêivis está aprendendo potências, mas continua desvirtuando do ponto principal do assunto e divagando sobre outras propriedades das potências. Dêivis leu em um livro que um número n1 é uma potência de n2 se n1 for divisível por n2 e se o quociente da divisão de n1 por n2 for uma potência de base n2. Como Dêivis é um cara cético, ele não acredita que isso pode ser verdade. Dessa forma, crie uma função acredita(n1,n2) que retorna a string "Pode Acreditar", caso n1 seja uma potência de n2; e a string "Fake News" caso contrário.

A Entrada consiste de:
Os parâmetros da sua função serão os números inteiros n1,n2≥2.

A Saída deve retornar:
A string "Pode Acreditar" (sem aspas duplas), caso n1 seja uma potência de n2; e a string "Fake News" caso contrário.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No primeiro exemplo, n1=8 e n2=2, e pode-se verificar que 8 é potência de 2, pois 8=23.
No segundo exemplo, n1=18 e n2=3, pois pelas propriedades da potênca definidas no enunciado, 18 não é uma potência de 3. As potências de 3 são: 1,3,9,27,81,....
No terceiro exemplo, n1=625 e n2=5, e pode-se verificar que 125 é potência de 5, pois 625=54.
'''
import math

def acredita(n1, n2):
    if n1 % n2 == 0 and (n2 ** (math.log(n1, n2))) == n1:
        return 'Pode Acreditar'
    else:
        return 'Fake News'

a = math.log(8, 2)
print(math.log(8, 2))

print(acredita(8, 2))