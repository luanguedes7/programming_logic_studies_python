'''
É hora de treinar !
Faustino gosta muito de malhar. Porém, ele não pode ir a academia pois tudo está fechado. Ele decidiu então fazer alguns exercícios em casa, e um deles é subir e descer escadas! Ele gosta muito de se exercitar mas ele gosta também de fazer treinos variados, então cada dia ele vai subir e descer apenas os n primeiros degraus da escada (peculiar, não ?). Faustino quer colocar uma imagem de quantos degraus ele vai subir, mas ele não desenha muito bem!

Você, grande amigo de Faustino, querendo que ele mantenha a forma, irá então criar uma função recursiva escada que recebe como parâmetro um número n e imprima uma escada com n degraus. Observe os casos de teste para entender melhor.

A Entrada consiste de:
Parâmetro da função recursiva escada que é apenas um número inteiro positivo n, o número de degraus que você deve imprimir.

A Saída deve apresentar:
Uma escada com n degraus.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.

Descrição dos Exemplos:
No segundo exemplo, a escada tem 6 degraus, então foram impressas 6 linhas cada uma contendo a quantidade de # correspondente a contagem de linhas impressas que começa em 1.
'''

def escada(n):
    if n == 1 or n == 0:
        print(n*'#')
    else:
        escada(n-1)
        print('#'*n )

escada(10)
