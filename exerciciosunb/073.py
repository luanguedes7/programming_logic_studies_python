#Aumentar o limite da recursividade
import sys
sys.setrecursionlimit(10**6)

#Função de fibbonacci por dicionários para n exceder o tempo de execução
valoresConhecidos = {0:0, 1:1}

def fibonacci(n):

    if n in valoresConhecidos:
        return valoresConhecidos[n]
    
    fibonacciCorrespondente = fibonacci(n-1) + fibonacci(n-2)
    valoresConhecidos[n] = fibonacciCorrespondente
    return fibonacciCorrespondente

n = int(input())
lista_n = tuple(map(int, input().split()))
lista_fib = list()

for i in lista_n:
    valorCorrespondente = fibonacci(i - 1)
    lista_fib.append(valorCorrespondente)

lista_fib = tuple(lista_fib)

print(lista_fib)