numeros = input()
numero_list = [float(numero) for numero in numeros.split(',')]
numero_list_distintos = sorted(set(numero_list))
tamanho_lista = len(numero_list)
if tamanho_lista == 1:
    print("Não é possível determinar o segundo maior valor com menos de dois elementos.")
elif len(numero_list_distintos) < 2:
    print("Não é possível determinar o segundo maior valor com menos de dois valores distintos.")
else:
    print(numero_list_distintos[-2])