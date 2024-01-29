def crearLista():
    lista=[]
    n=int(input("Cuantos elementos tiene la lista?"))
    for x in range(n):
          valor=int(input("Introduce un elemento de la lista:"))
          lista.appeand(valor)
    return lista

#función que devuelve el rpoducto de sus elementos
def producto(lista):
    p=1
    for x in range(len(lista)):
         p=p*lista[x]
    return p
    
#Progama principal
lista=crearLista()
print(lista)
print("Palabras con caracteres:",mascaracteres(palabras))
