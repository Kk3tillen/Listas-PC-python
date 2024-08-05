valor = 1
maior_valor = 0;
while valor != 0:
    valor = float(input())
    if valor >= maior_valor:
        maior_valor = valor
if maior_valor != 0:
    print('O seu maior gasto hoje foi R$ {:.2f}'.format(maior_valor))
else:
    print('Você não teve gastos hoje!')