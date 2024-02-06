def cargar_palabras():
    palabras=[]
    longitud=1;
    while longitud>0:
        palabra=input("Introduce una palabra:")
        longitud=len(palabra)
        palabras.append((palabra,longitud))
    return palabras
def visualizar_palabras(palabras):
    for palabra in palabras:
        totalVotos=0
        if palabra[1]>5:
            print(palabra[0])

            
palabras=cargar_palabras()
visualizar_palabras(palabras)
