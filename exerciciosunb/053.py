def não_possui_a_letra_u(palavra):
    for letra in palavra:
        if letra.lower() == 'u'or letra.lower() == 'ú' or letra.lower() == 'ü' or letra.lower() == 'û' or letra.lower() == 'ù':
            return False
    return True

print(não_possui_a_letra_u("Universidade"))