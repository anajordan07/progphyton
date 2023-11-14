num=int(input("Introduce un número de 1 o 2 dígitos:"))
if num>0:
    if num<100:
        if num>=10:
            print("El número tiene dos cifras")
        else:
            print("El número tiene una cifra")
    else:
        print("El numero tiene mas de dos cifras")
else:
    print("El número es negativo")
    
