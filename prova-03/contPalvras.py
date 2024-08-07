frase = input()
palavras = frase.split()
palavras_impressas = set()

for palavra in palavras:
    if palavra not in palavras_impressas:
        qnt_palavras = palavras.count(palavra)
        print(f"{qnt_palavras}: {palavra}")
        palavras_impressas.add(palavra)