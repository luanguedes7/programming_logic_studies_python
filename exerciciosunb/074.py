import csv

alunos = []
reprovados = []

with open(input(), mode='r') as arquivo:
    leitura = csv.reader(arquivo)
    presenca = []
    numeroDepresencas = 0

    for i in leitura:
        presenca += i
        numeroDepresencas += 1



for i in presenca:
    if not i in alunos:
        alunos.append(i)

for i in alunos:
    idas = presenca.count(i)

    if idas/numeroDepresencas < 0.75:
        reprovados.append(i)

if len(reprovados) == 0:
    print('Nenhum aluno reprovado por faltas')
else:
    for i in reprovados:
        print(i)
    
