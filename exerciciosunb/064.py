'''
Sala de Espera
Bruna precisa fazer um exame de sangue. Ela chegou no laboratório, e foi pedido que ela espere na sala de espera. Essa sala possui m fileiras com n cadeiras cada. O espaço entre cada cadeira é de 1m.

Como ainda estamos em pandemia, Bruna gostaria de se sentar o mais distante possível de outras pessoas, mas ela está há muito tempo sem comer, e não consegue mais pensar com clareza para decidir o melhor lugar, então você vai ajudá-la, encontrando o lugar vago em alguma das m fileiras que maximize a distância para qualquer vizinho na mesma fileira.

Entrada

A primeira linha da entrada possui dois inteiros: m e n, o número de fileiras, e a quantidade de cadeiras em cada fileira, respectivamente. (1≤m≤10 ; 2≤n≤100 ).

As próximas m linhas da entrada contém n inteiros cada, as m fileiras da sala. Cada fileira é representada por n inteiros, a0,a1,...an−1, onde ai∈{0,1}. Se ai=0 o lugar está desocupado, e Bruna pode se sentar nele. Caso contrário, o lugar está ocupado. É garantido que haverá pelo menos 1 espaço vazio em cada fileira.

Saída

imprima a maior distância que Bruna pode ficar de qualquer outra pessoa em uma fileira.

Observações

No primeiro exemplo de teste, a maior distância possível para outra cadeira ocupada ocorre quando Bruna senta na primeira cadeira da primeira fila;
No segundo exemplo de teste, Bruna consegue se sentar, no máximo, a 1 metro de qualquer outra cadeira ocupada.
'''