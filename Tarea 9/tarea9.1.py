# Definir lista vacía
lista=[]
for x in range(5):
    valor=float(input("Itroduce una altura:"))
                lista.appeand(valor)
suma=0
for x in range(5):
    suma=suma+lista[x]
promedio=suma/5
    print("La altura media es",promedio

supera=0
nosupera=0
for x in range (5):
          if lista[x]>promedio:
          supera=supera+1
        else:
            nosupero=nosupero+1
print("Personas superior a la media.",supera)
print("Personas inferior a la media.",nosupera)
