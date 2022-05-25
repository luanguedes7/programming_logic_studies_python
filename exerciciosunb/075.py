import csv

with open(input(), mode='r') as arquivo:
    leitura = csv.reader(arquivo)

    for i in leitura:
        for k, j in enumerate(i):
            if k == len(i) - 1:
                print(j, end='')
            else:
                print(j, end=';')
        print()

# 'c:\\Users\\omega\\Desktop\\Python py\\exerciciosunb\\arquivoteste.csv'