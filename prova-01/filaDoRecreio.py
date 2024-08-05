n_alunos = int(input())

for _ in range(n_alunos):
    n_notas = int(input())
    
    notas = list(map(int, input().split()))
    notas_ordenadas = sorted(notas, reverse=True)
    
    resultado = [x - y for x, y in zip(notas, notas_ordenadas)]
    pessoa_no_mesmo_lugar = resultado.count(0)
    print(pessoa_no_mesmo_lugar)
