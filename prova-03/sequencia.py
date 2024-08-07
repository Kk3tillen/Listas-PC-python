n = int(input())
aux = n
print(f"{int(aux)}->", end="")
while aux != 1:
    if aux % 2 == 0:
        aux = aux / 2
        if aux == 1:
            print(f"{int(aux)}", end="")
        else:
            print(f"{int(aux)}->", end="")    
    else:
        aux = (aux *3)+1
        if aux == 1:
            print("oi :0") 
        print(f"{int(aux)}->", end="")

