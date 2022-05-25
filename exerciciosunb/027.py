'''
Uma vida musical
Gustavo e Nathan são estudantes de Ciência da Computação na UnB, mas o último semestre que eles fizeram foi muito puxado e eles estão muito cansados. Eles decidiram então, como grandes amigos, tomar um ano sabático e rodar pelo Brasil tentando fazer o que eles gostam, música. Como são estudantes, não terão muito recursos, então sempre irão trocar seus instrumentos com outros artistas para ter novas experiências e aprender novos instrumentos. Mas isso trouxe um problema, pois as vezes o novo instrumento pode não caber no carro deles. Você irá então ajudá-los! Crie um função areaInstrumento que irá receber três argumentos: dois inteiros n,m correspondendo ao instrumento de forma retangular usado por Nathan e um inteiro r correspondendo ao lado do triângulo equilátero que equivale ao instrumento que Gustavo toca. Calcule a área de ambos os instrumentos e retorne a soma deles.

A Entrada consiste de:
Nos parâmetros da função areaInstrumento que são os três números inteiros n, m e r (2≤n,m,r≤100) como descritos no enunciado..

A Saída deve retornar:
A soma da área de ambos os instrumentos.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.
Atenção, a criação de uma função com o nome determinado pelo enunciado é fundamental para a prática do aluno e o Moodle irá descontar pontos caso a criação não tenha sido feita corretamente (sendo case-sensitive o nome da função).
Submeta SOMENTE o que foi solicitado.
Não se preocupe com arredondamentos, o próprio juiz fará o truncamento para 5 casas decimais.
Use o método sqrt(x) da biblioteca math para auxiliar no cálculo da área do triângulo.
'''
import math

def areaInstrumento(n, m, r):
    '''n, m  intrumento retangular tocado por Nathan
       r lado do triângulo equilátero que corresponde ao instrumento que Gustavo toca 
    '''
    areaInstrumentoNathan = n * m
    areaInstrumentoGustavo = (r ** 2) * math.sqrt(3)/4
    return areaInstrumentoNathan + areaInstrumentoGustavo

print("{0:.5f}".format(areaInstrumento(5,5,3)))
