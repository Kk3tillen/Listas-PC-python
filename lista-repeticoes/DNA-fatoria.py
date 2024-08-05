n = int(input())
fatorial = 1
for i in range(1, n+1):
    fatorial = fatorial * i

if n == 0:
    print('O número deve ser maior que 0.')
else:
    print(f'Resultado do fatorial: {fatorial}')
