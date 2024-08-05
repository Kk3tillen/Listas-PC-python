def get_range(n, cells, distance, user):
    inicio = user - distance
    fim = user + distance
    indices = [i for i in range(n) if inicio <= cells[i] <= fim]
    
    if indices:
        return [cells[i] for i in indices]
    else:
        return "USUARIO DESCONECTADO"


n, d, u = map(int, input().split())
cells = [int(input()) for _ in range(n)]

resultado = get_range(n, cells, d, u)
if resultado == "USUARIO DESCONECTADO":
    print(resultado)
else:
    print(" ".join(map(str, resultado)))
