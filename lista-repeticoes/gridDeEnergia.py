n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        valor = abs(i - j) + 1
        print(valor, end=' ')
    print()
