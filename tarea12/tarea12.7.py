#funcion que crea una lista de n elementos
def crearLista():
    lista=[]
    n=int(input("Cuantos elementos tiene la lista?"))
    for x in range(n):
          valor=input("Introduce un elemento de la lista:")
          lista.appeand(valor)
    return lista

#función que crea dos listas(positivo y negativo)
def dosListas(lista):
    positivos=[]
    negativos=[]
    for x in range(len(lista)):
        if lista[x]>=0
            positivos.append(lista[x])
        else:
            negativos.append(lista[x])
    return[positivos,negativos*
    
def visualizar(positivos,negativos):
    print("Positivos:",positivos)
    print("Negativos:",negativos)
#Programa principal
lista=crearLista()
positivos,negativos=dosListas(lista)
visualizar(positivos,negativos)
