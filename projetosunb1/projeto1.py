# Definição dos dias: Colunas da Tabela - 6 colunas
# As strings já estão com certos espaços de modo a facilitar na mostragem da grade. A lista "dias" não fará parte da matriz definida a seguir
dias = [' Seg     ', ' Ter     ', ' Qua     ',
        ' Qui     ', ' Sex     ', ' Sab     ']

# Definição dos horários: Linhas da Tabela - 15 linhas. Note que está apresenta um espaço antes e outro depois do conteúdo para mostragem na grade.
horarios = [' 08:00 - 08:55 ', ' 08:55 - 09:50 ', ' 10:00 - 10:55 ', ' 10:55 - 11:50 ', ' 12:00 - 12:55 ',
            ' 12:55 - 13:50 ', ' 14:00 - 14:55 ', ' 14:55 - 15:50 ', ' 16:00 - 16:55 ', ' 16:55 - 17:50 ',
            ' 18:00 - 18:55 ', ' 19:00 - 19:50 ', ' 19:50 - 20:40 ', ' 20:50 - 21:40 ', ' 21:40 - 22:30 ']

#Definição de algumas listas a serem usadas nas funções do cógico
diasInteiros = []
horasInteiras = []
horasInteirasCorrigidas = []
materiasComProblemas = []

# Criação da Grade Horária: Matriz 15 x 6
gradeHoraria = [6 * ['          '] for i in range(15)]

#Inserção dos horários na matriz criada anterior, de modo a forma uma única.
[gradeHoraria[i].insert(0, horarios[i]) for i in range(15)]


def printagrade(gradeHoraria, dias):
    ''' Mostrará a grade horário para o usuário'''

    #Se houve alguma matéria com problema, printará antes da grade
    if len(materiasComProblemas) != 0:
        for i in materiasComProblemas:
            print('!' + f'({i})')

    #Print dos dias
    moldura = '+---------------+' + '----------+' * 6

    print(moldura)
    print('|               |', end='')

    for d in dias:
        print(d + " |", end='')
    print()

    print(moldura)

    #Print da matriz, nas linhas que há matérias
    for l in range(15):
        if verificaLinha(gradeHoraria[l]) == False:
            for c in range(7):
                if c == 0:
                    print('|' + gradeHoraria[l][c] + '|', end='')
                elif 1 <= c <= 5:
                    print(gradeHoraria[l][c] + '|', end='')
                else:
                    print(gradeHoraria[l][c] + '|', end='')
                    print()
                    print(moldura)


def verificaLinha(gradeHoraria):
    '''Verifica se há matérias na linha da grade horária'''

    for k in range(1, 7):
        if gradeHoraria[k] == '          ':
            linhaSemMateria = True
        else:
            linhaSemMateria = False
            break
    
    return linhaSemMateria


def separaHorario(DTH):
    ''' Fragmentar o horário antes e depois 'M', 'T' e 'N' '''
    turno = ''

    for s in DTH:
        if s.isalpha():
            turno = s
            indiceTurno = DTH.index(s)

    for s in DTH[0:indiceTurno]:
        diasInteiros.append(int(s))

    for s in DTH[indiceTurno + 1:len(DTH)]:
        horasInteiras.append(int(s))

    horariosMTN(turno)


def horariosMTN(Turno):
    '''Incrementa ou decrementa um valor dos horários(horasInteiras) para a lógica de inserção na grade'''

    if Turno.upper() == 'M':
        for i in horasInteiras:
            x = i - 1
            horasInteirasCorrigidas.append(x)
    elif Turno.upper() == 'T':
        for i in horasInteiras:
            x = i + 4
            horasInteirasCorrigidas.append(x)
    elif Turno.upper() == 'N':
        for i in horasInteiras:
            x = i + 10
            horasInteirasCorrigidas.append(x)


def alteraGrade(comando, gradeHoraria, codMat, d, h):
    ''' Essa função altera a grade horária a partir do comando de entrada. Se for +, adiciona. Se for - retira'''
    
    if comando == '+':
        if gradeHoraria[h][d] == '          ':
            gradeHoraria[h][d] = codMat

    if comando == '-':
        if gradeHoraria[h][d] != '          ' and gradeHoraria[h][d] == codMat:
            gradeHoraria[h][d] = '          '
  

def podeAlt(comando, gradeHoraria, codMat, d, h):
    '''Essa função vai indicar se é possível ou não alterar a grade horária'''

    if comando == '+':
        if gradeHoraria[h][d] == '          ':
            return True
        else:
            return False

    if comando == '-':
        if gradeHoraria[h][d] != '          ' and gradeHoraria[h][d] == codMat:
            return True
        else:
            return False


while True: 
    entUsuario = input()

    if entUsuario == '?':
       printagrade(gradeHoraria, dias) 
       materiasComProblemas = [] #Toda vez que o usuário printar, há um "reset" nessa lista

    elif entUsuario == 'Hasta la vista, beibe!':
        break

    else:
        entUsuario = entUsuario.split()
        comando = entUsuario[0]
        codMat = ' '+ entUsuario[1] + ' '

        for i in range(2,len(entUsuario)):
            #Todas as vezes que entrar um novo horário, dou um "reset" nas listas para que não haja conflito 

            diasInteiros = []
            horasInteiras = []
            horasInteirasCorrigidas = []
            estaMateriaComProblema = False
            codHorario = entUsuario[i]
            horasInteiras = []
            diasInteiros = []
            separaHorario(codHorario)

            for h in horasInteirasCorrigidas:
                for d in diasInteiros:
                    d -= 1
                    if podeAlt(comando, gradeHoraria, codMat, d, h):
                        alteraGrade(comando, gradeHoraria, codMat, d, h)
                    else:
                        materiasComProblemas.append(f'{comando + codMat + codHorario}')
                        estaMateriaComProblema = True #Se houver erro na matéria uma vez, já saio do loop pois não é possível sua adição
                        break
                if estaMateriaComProblema:
                    break
                    

