'''
Média aritmética
Emidio está dando um curso de "como ser um Emidio". Ele acredita que precisa fazer avaliações rigorosas, para ter certeza de que seus alunos estão aprendendo tudo corretamente. Para ter uma ideia de como os alunos estão se saindo, ele resolveu calcular a média da primeira prova. O problema é que Emidio não se deu ao trabalho de contar quantos alunos estão fazendo o seu curso.

Já sabe, né? O Emidio é o Emidio... É claro que ele pediu a sua ajuda para esta tarefa.

Entrada
A entrada é composta por um número 2≤n≤106 desconhecido de linhas. Cada linha indica a nota  0≤x≤103 de um aluno, exceto a última, que contém somente o número -1 para indicar que não há mais notas a serem lidas.

Saída
Escreva um programa que leia a entrada e imprima a parte inteira da média aritmética dos alunos de Emidio.

Notas
O valor -1 não deve ser considerado para a média.
'''
soma_das_medias = 0
quantidade_de_notas = 0
while True:
    nota = input()
    if nota == '-1':
        break
    nota = int(nota)
    soma_das_medias += nota
    quantidade_de_notas +=1

print(f'{int(soma_das_medias / quantidade_de_notas)}')


