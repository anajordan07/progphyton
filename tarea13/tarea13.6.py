def cargar_productos():
    productos=[]
    for x in range (5):
        producto=input("Introduce el nombre del producto:")
        precio=int(input("Precio del procucto"))
        productos.append((producto,precio))
    return producto
def visualizar_productos(productos):
    print("lista de todos los productos")
    for producto in productos:
        print(prodcto[0],"tiene un precio:",producto[1])

def visualizar_productos_ofertas(productos):
    for producto in productos:
        prod=producto[1]
        il(prod>=10 and prod<=15):
            print(producto[0],"tiene un precio:",producto[1])

productos=cargar_productos()
visualizar_productos(productos)
visualizar_productos_ofertas(productos)
