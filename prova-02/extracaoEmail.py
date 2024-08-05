def extracaoParteEmail(email):
    inicio = email.find("@") + 1
    fim = email.find(".", inicio)
    return email[inicio:fim]

email = input()
while email != "FIM":
    print(extracaoParteEmail(email))
    email = input()