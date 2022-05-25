'''
A Entrada consiste de:
Uma linha contendo um número real positivo.

A Saída deve apresentar:
Uma linha com a mensagem "X = ?", onde ? deve ser substituído pela medida em kcal com formatação de 2 casas decimais.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos definidos.
1 J = 0,238 845 896 627 cal

Descrição dos Exemplos:
Os exemplos são autoexplicativos. Dada a entrada basta aplicar na equação.

'''
i = float(input())

kcal = (i*0.238845896627) /1000

print(f'X = {kcal:.2f}')