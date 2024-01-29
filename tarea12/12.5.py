#Funcion creamos una lista de n empleados
def crearLista(n):
    articulos=[]
    precios=[]
    for x in range(n):
        articulo=input("Introduce el nombre de un articulo:")
        precio=int(input("Introduce elprecio del articulo:"))
        articulos.append(articulo)
        precios.append(precio)
    return[articulos,precios]


#funcion visualizar los articulos y sus precios
def verArticulo(articulos,precios):
    for x in range(len(articulos)):
        print(articulos[x],".",precios[x])

#funcion articulo mas caro
    def articuloMasCaro(articulos,precios):
        masCaro=precios[0]
        pos=0
        for x in range(1,len(precios)):
            if precios[x]>masCaro:
                masCaro=precios[x]
                pos=x
        print("El articulo mas caro es",articulo[pos],"con un precio de",masCaro)

#funcion articulo con precio menoor a uno
        def articulosMenores(articulos,precio,importe):
            for x in range(len(precios)):
                if precios[x]<importe:
                    print(articulos[x],"tiene un precio menor a",importe,"y es",precios[x])

#Programa principal
n=int(input("Cuantos articulos hay?"))
articulos,precios=crearLista(n)
verArticulo(articulos, precios)
articuloMasCaro(articulos, precios)
importe=int(input("Importe a comprar:"))
articulosMenores(articulos,precios,importe)
