def collatz(s, n, cont):
    if n <= cont :
        return int(s)
    else:
        if s % 2 == 0: #é par
            return collatz(s/2, n, cont+1)
        else:
            return collatz(3*s - 1, n, cont+1)


print(collatz(12, 5, 1))