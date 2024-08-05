
coordenadas = input()
pontos_quaisquer = input()
x1, y1, x2, y2 = coordenadas.split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

x, y = pontos_quaisquer.split()
x = float(x)
y = float(y)

if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
    print('Dentro!')
else:
    print('Fora!')
