pedidos = dict()
pedidos['hamburguer(s)'] = int(input())
pedidos['batata(s)'] = int(input())
pedidos['refrigerante(s)'] = int(input())
pedidos['milkshake(s)'] = int(input())
pedidos['salada(s)'] = int(input())

for c, v in sorted(pedidos.items()):
    if not (v == 0):
        print(f'Pedido com {v} {c}!') 