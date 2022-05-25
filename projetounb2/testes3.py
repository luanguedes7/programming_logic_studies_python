import csv
from operator import itemgetter

arqLido = []
arqsLidos = []

def lerAqr(arquivo):
    with open('C:\\Users\\omega\\Desktop\\Python py\\projetounb2' + f'\\{arquivo}', mode='r', encoding='utf-8') as arq:
        rArq = csv.reader(arq)

        for e, i in enumerate(rArq):
            if e != 0:
                arqLido.append(i)


def mostraMatDoc(docente):
    ''' Função responsável por mostrar a carga de um "docente" '''

    gradeDocente = dict()
    haDocente = False  # Flag para verificar se há algum docente
    cargaTotal = 0
    nAlunos = 0

    if not (docente in gradeDocente):
        gradeDocente[docente] = []

    for i in arqLido:
        if docente in i[4]:
            gradeDocente[docente] += [i]
            haDocente = True

    if haDocente:
        print(docente + ':')

        materiaAnterior = ''
        for i in sorted(gradeDocente[docente], key=lambda x: (x[1], x[2])):

            materiaAtual = f' * {i[1]} ({i[0]}):'

            # print da matéria(com uma verifição para não printar duas vezes o mesmo nome de matéria)
            if materiaAtual != materiaAnterior:
                print(f' * {i[1]} ({i[0]}):')
                materiaAnterior = materiaAtual

            # Obtenção da carga horário a partir do nome do docente(Está contido nessa string)
            carga = i[4][len(i[4]) - 5: len(i[4])].replace('h)', '')
            carga = carga.replace('(', '')
            carga = carga.strip()

            # print da turma, carga horária e número de alunos
            print(5*' ' + f'Turma {i[2]}' + ':' + f' {carga}h ({int(i[7])} alunos)')

            if int(i[7]) >= 6:
                cargaTotal += int(carga)
                nAlunos += int(i[7])

        print(f'[Carga total considerada: {cargaTotal}h ({(cargaTotal/nAlunos):.2f}h/aluno)]')

    else:
        print(f'No hay {docente}...')


def disc(d):
    '''Função responsável por mostrar as turmas com "d" ou mais professores'''

    dDoc = dict()
    matAnt = ''
    profAnt = ''
    profT = 1
    entrou = False

    for i in sorted(arqLido, key=lambda x: (x[1], x[2], x[4])):
        matTur = f'{i[1]} ({i[0]}) {i[2]}'
        profAtual = f'{i[4].split()[0]} {i[4].split()[1]}'

        if not matTur in dDoc:
            dDoc[matTur] = 0

        if matTur == matAnt and profAtual != profAnt:
            profT += 1
            entrou = True
        else:
            profT = 1

        if entrou:
            dDoc[matTur] = profT
            entrou = False

        matAnt = matTur
        profAnt = profAtual

    if d in dDoc.values():
        print(f'Turmas com pelo menos {d} docentes:')
        matAnt1 = ''
        k = 1
        listaDeTurmas = list()

        for i in dDoc.items():
            if i[1] >= d:
                materia = i[0].split()[:]
                turma = materia.pop()
                materia = ' '.join(materia)

                # Verificação para não printar a mesma matéria várias vezes
                if materia != matAnt1:
                    if k == 1:
                        print(' * ' + materia + ':', end='')
                        k += 1
                    else:
                        print()
                        print(' * ' + materia + ':', end='')
                        listaDeTurmas.clear()
                else:
                    print(',', end='')  # Vírgula presente após cada turma

                # print da turma juntamente com a quantidade de professores
                print(f' {turma} ({i[1]})', end='')

                matAnt1 = materia
    else:
        print(f'No hay {d}...')


def alunosMatriculados(cod):
    '''Função responsável por mostrar quantos alunos há em determinado "cod" '''
    aluMat = dict()
    alunos = 0
    mat = cdg = False

    if not (cod in aluMat):
        aluMat[cod] = []

    for i in arqLido:
        if cod in i[0]:
            aluMat[cod] += [i]

    turmaAnterior = ''
    for i in sorted(aluMat[cod], key=itemgetter(2)):
        turmaAtual = i[2]

        if turmaAtual != turmaAnterior:
            alunos += int(i[7])
            turmaAnterior = turmaAtual

        cdg = i[0]
        mat = i[1]

    if mat and cdg:
        saida = f'{int(alunos)} matriculados em {mat} ({cdg})'
        return saida
    else:
        return False

while True:
    entrada = input()

    if entrada == 'FIM':
        break

    elif 'leia' in entrada:
        ler = entrada.split()[1]
        arqsLidos += [ler]

        if arqsLidos.count(ler) == 1:
            lerAqr(ler)
        
    elif 'carga' in entrada:
        mostraMatDoc(entrada.split(maxsplit=1)[1])
    
    elif 'disciplina' in entrada:
        disc(int(entrada.split(maxsplit= 1)[1]))
    
    elif 'matriculas' in entrada:
        mats = entrada.split()
        matriculas = []

        for e,i in enumerate(mats):
            if e !=0:
                if alunosMatriculados(i):
                    matriculas += [alunosMatriculados(i).split()]
                else:
                    print(f'No hay {i}...')
        
        for i in matriculas:
            i[0] = int(i[0])
            
        for i in sorted(matriculas, key= lambda x:(-x[0], x[3])):
            i[0] = str(i[0])
            print(' '.join(i))