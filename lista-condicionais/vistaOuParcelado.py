valor = int(input())
tipo_compra =(input())

if tipo_compra.upper() == "V":
    valor_compra = int(valor - (valor * 0.05))
    print(f'Valor à pagar:{valor_compra}')
else: 
    valor_compra = int(valor + (valor * 0.08))
    print(f'Valor à pagar:{valor_compra}')
    for x in range(1,4):
        print(f'Parcela {x}:{int(valor_compra/3)}')