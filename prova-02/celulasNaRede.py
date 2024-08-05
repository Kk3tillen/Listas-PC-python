def get_range(n, cells, distance, user):
    inicio = user - distance
    fim = user + distance
    indices = [i for i in range(n) if inicio <= cells[i] <= fim]
    
    if indices:
        return [cells[i] for i in indices]
    else:
        return "USUARIO DESCONECTADO"


N, D, U = map(int, input().split())
cells = [int(input()) for _ in range(N)]

resultado = get_range(N, cells, D, U)
if resultado == "USUARIO DESCONECTADO":
    print(resultado)
else:
    print(" ".join(map(str, resultado)))
