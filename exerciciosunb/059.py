'''
Presente especial
O aniversário do Quirino está chegando e Faustino quer presentear seu grande amigo com um presente muito especial. Isso mesmo, o melhor e mais desejado presente que alguém possa querer: uma lista de inteiros! Faustino percorreu os quatro cantos do mundo para pegar os melhores inteiros, porém agora ele está muito cansado e lembrou que Quirino só gosta de listas ordenadas. Como o aniversário de Quirino é amanhã e Faustino está muito cansado após pegar todos os inteiros, você ficou encarregado do trabalho.

Entrada

A entrada contém apenas de uma linha de inteiros separados por espaço. É garantido que o tamanho da lista não passa de 105.

Saída

Imprima a lista após arrumá-la.

'''
numeros = list(map(int, input().split()))
numeros.sort()
print(numeros)

