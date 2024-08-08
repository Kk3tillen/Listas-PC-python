frase = input()
palavras_impressas = set()

def encontrarPalavra(frase, palavras_impressas):
    palavras = frase.split()
    for palavra in palavras:
        if palavra not in palavras_impressas:
            qnt_palavras = palavras.count(palavra)
            print(f"{qnt_palavras}: {palavra}")
            palavras_impressas.add(palavra)

encontrarPalavra(frase, palavras_impressas)
