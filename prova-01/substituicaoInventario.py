texto = input()
value1 = input()
novo_value = input()
if value1 in texto:
    texto = texto.replace(value1, novo_value).replace("[", "").replace("]", "")
    list_texto = [palavra.strip() for palavra in texto.split(',')]
    print(list_texto)
else : 
    print("Item não presente no inventário.")