'''
 múltiplo de 5? Como descobrir usando recursividade mútua?
Uma forma de se descobrir se um número é múltiplo de 5 é ir diminuindo ele de 5 até que não se possa mais subtrair 5 sem que o resultado seja negativo. 

Por exemplo o número 15, será que ele é múltiplo de 5? É só ir subtraindo 5 para ver se chega no zero, se chegar no zero é múltiplo de 5! 15 - 5 = 10; 10 - 5 = 5, 5 - 5 = 0! Ou seja a sequência gerada  terminou em zero, logo 15 é múltiplo de 5.

E o número 14, é múltiplo de 3? A sequência gerada é 14, 11, 6, 1; ou seja, não termina em zero, logo não é múltiplo de 3.

Vendo estas sequências, Zezinho, que está tentando identificar um padrão para implementar uma solução usando recursividade mútua (duas ou mais funções sendo que uma chama a outra), tentou solucionar o problema da seguinte forma:

def multiplo5(n):
    if n == 0:
        return True
    elif n == 1 or n == 2 or n == 3 or n== 4:
        return False
    else:
        return não_multiplo5(n-5)
    
def não_multiplo5(n):
    if n==0:
        return False
    elif n==1 or n==2 or n == 3 or n==5:
        return True
    else:
        return multiplo5(n-5)
Mas esta solução funciona para o número 15, por exemplo, mas não funciona para o número 10. Verifique por que isto acontece. Ache um padrão de sequência para que não aconteça o problema verificado e implemente a recursão mútua de forma que ela funcione corretamente.

A Entrada consiste de:
de uma função mutuamente recursiva que pode ser ou multiplo5(n) ou não_multiplo5(n) onde n é o número que se quer verificar se é múltiplo de 5.

A Saída deve apresentar:
para a função multiplo5 True, se for múltiplo de 5 e False, se não for múltiplo de 5 e;
para a função não_multiplo5 False, se for múltiplo de 5 e False, se for múltiplo de 5.
Exemplo:
o enunciado e o texto são auto-explicativos.
'''
def multiplo5(n):
    if n == 0:
        return True
    elif n == 1 or n == 2 or n == 3 or n== 4:
        return False
    else:
        return not não_multiplo5(n-5)
    
def não_multiplo5(n):
    if n==0:
        return False
    elif n==1 or n==2 or n == 3 or n==4:
        return True
    else:
        return not multiplo5(n-5)

print(multiplo5(5))
print(não_multiplo5(5))
print(multiplo5(20))
