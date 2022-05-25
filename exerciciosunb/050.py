'''Debuggar'''
def tem_letra_maiúscula(s):
    for letra in s:
        cont = 0 #qtd de letras maiúsculas
        if letra.isupper():
            return True
    
    return False
            