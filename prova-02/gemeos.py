def ehPrimo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primoGemeo(num):
    if ehPrimo(num) and ehPrimo(num + 2):
        return "Número forma par de gêmeos"
    else:
        return "Número não forma par de gêmeos"
    
print(primoGemeo(int(input())))
