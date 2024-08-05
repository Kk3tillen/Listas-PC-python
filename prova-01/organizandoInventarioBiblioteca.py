import ast

string_com_listas = input()
listas_aninhadas = ast.literal_eval(string_com_listas)

def juntar_listas(lista_atualizada):
    resultado = []
    while any(isinstance(i, list) for i in lista_atualizada):
        lista_atualizada = [item for sublist in lista_atualizada for item in (sublist if isinstance(sublist, list) else [sublist])]
    resultado.extend(lista_atualizada)
    return resultado
lista_unica = juntar_listas(listas_aninhadas)
print(lista_unica)
