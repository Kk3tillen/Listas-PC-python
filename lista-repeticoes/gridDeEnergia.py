n = int(input("Digite o valor de n: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        # Calcular o valor correto para cada célula da matriz
        valor = abs(i - j) + 1
        print(valor, end=' ')
    print()  # Nova linha após cada linha da matriz
