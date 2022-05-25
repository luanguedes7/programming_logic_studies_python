# Fibonacci III
termo = int(input())

lista_fibonacci = []
def fibonacci(n):
    if n == 0 or n == 1:
        lista_fibonacci.append(n)
        return n
    else:
        lista_fibonacci.append(n)
        return fibonacci(n-1) + fibonacci(n-2)

termof = fibonacci(termo)
print(f'Termo: {termof}')

print(f'Quantidades:')
lista_fibonacci.sort()
for i in range(len(lista_fibonacci) - 1):
    if lista_fibonacci[i] != lista_fibonacci[i + 1]:
        print(f'fibonacci({lista_fibonacci[i]}) - {lista_fibonacci.count(lista_fibonacci[i])}')
print(f'fibonacci({termo}) - 1')
