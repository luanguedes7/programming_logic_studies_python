'''
Estatísticas II
Dado um conjunto de números de inteiros X={x1,x2,…,xN}, podemos calcular seu desvio padrão (σ) como:

σ=∑i=1N(xi−x¯)2N−−−−−−−√

em que x¯ representa a média dos valores de X.

Dessa forma, escreva um programa que calcule a média e a variância de X

Entrada
A entrada consiste de N ( 1≤N≤100 ) números inteiros x1,x2,…,xN (103≤xi≤103,i=1,…,N) separados por espaço em branco.

Saída
Imprima duas linhas, em que cada uma contém um valor em ponto flutuante com uma casa decimal de precisão. A primeira linha deve apresentar a média de X, enquanto que a segunda linha deve apresentar o desvio padrão de X.

Observações

No primeiro caso de teste, a média dos valores da lista é (16+24+30)/3 = 20.0. O desvio padrão é calculado por (16−20)2+(24−20)2+(20−20)2)/3−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−√ = 3.3. 
'''
lista = list(map(int, input().split()))

#primeira parte
somatório_lista = sum(lista)
media = somatório_lista/len(lista)

#segunda parte
numerador = 0
denominador = len(lista)
for i in lista:
    valor_atual = (i - media)**2
    numerador += valor_atual

num_div_den = numerador / denominador

desvio_padrao = num_div_den ** 0.5 #Raiz quadrada sem utilizar módulo math



#saida
print(f'{media:.1f}')
print(f'{desvio_padrao:.1f}')