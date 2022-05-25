import math

def TwoDSpace(deslocamento, amplitude, espaço):
    dicionario ={}
    for i in range(20):
            j = int(deslocamento - amplitude*math.sin(10*i*math.pi/180))
            dicionario[i, j] = espaço
    for j in range(20):
        for i in range(40):
            print(dicionario)
            
TwoDSpace(10, 8, ".")