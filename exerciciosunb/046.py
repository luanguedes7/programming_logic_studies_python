def positivo(n):
    if n >= 0:
        return True
    else:
        return False

acumulador = 0
achou_positivo = False
cont = 0
n = 0
x = input()

while True :
    n += 1 
    if x == 'f':
        break
    else: 
        x = int(x)

    achou_positivo = positivo(x)

    if achou_positivo:
        cont += 1
        acumulador += x
    
    x = input()

#cont += 1
if n == 1:
    print(0.0)
else:
    media_positivo = acumulador/cont
    print(media_positivo)