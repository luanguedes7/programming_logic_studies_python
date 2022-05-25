'''
Tempo de limpeza II
O jovem Viníulus é o responsável por preparar o almoço para seus pais em tempos de pandemia. Ultimamente, Viníulus esta bastante estressado por ter que cuidar de todos os almoços e os pratos estão cada dia mais simplificados. Viníulus recebeu algumas reclamações de seus pais e agora pretende organizar melhor seu tempo.

Elabore um programa que estima o tempo que ele irá levar para preparar o almoço sabendo que cada prato leva em média de 5 à 15 minutos para ser preparado.


A Entrada consiste de:
Um número inteiro indicando o número de pratos (pratos>0) para serem preparados

A Saída deve apresentar:
A quantidade de horas gastas no melhor e pior caso, com precisão de duas casas decimais.

Observações:
Não é necessário validar se os valores de entrada estão dentro dos intervalos e tipos definidos.

Descrição dos Exemplos:
No primeiro exemplo, Viníulus tem que preparar 2 pratos. No melhor caso ele demora 0.17 horas para lavar e no pior caso ele demora 0.50 horas.
'''
pratos = int(input())
melhor_media = 5 * 0.0166667
pior_media = 15 * 0.0166667

melhor_tempo = pratos * melhor_media
pior_tempo = pratos * pior_media

print(f'Entre {melhor_tempo:.2f} e {pior_tempo:.2f}')
