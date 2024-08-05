numeros = input()
numero_list = [float(numero) for numero in numeros.split(',')]
maior_numero = max(numero_list)
print(maior_numero)
