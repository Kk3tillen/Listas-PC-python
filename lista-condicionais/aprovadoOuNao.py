SOMA_PESOS = 9
n1 = (float(input()))
n2 = (float(input()))
n3 = (float(input()))
media = ((n1*2) + (n2*3) + (n3*4))/SOMA_PESOS

if media >= 7:
    print('Francisco está aprovado')
elif media < 3:
    print('Francisco está reprovado')
else:
    print('Francisco está em prova final')