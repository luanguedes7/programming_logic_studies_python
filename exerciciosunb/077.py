import os

def caminho(caminho):
    if os.path.abspath(caminho):
        print(f'Voce esta no {caminho}')
    else:
        print('Apaguei?')  