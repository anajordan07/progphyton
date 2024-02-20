#Clase Triangulo con tres propiedades:lado1,lado2 y lado3
class Triangulo:
   def _init_(self,l1,l2,l3):
        self.lado1=l1
        self.lado2=l2
        self.lado3=l3

    def imprimirMayor(self):
        print("Medida del lado mayor:")
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print(self.lado1)
        else:
            if self,lado2>self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

    def equilatero(self):
        if (self.lado1==self.lado2. and self.lado1==self.lado3):
            print("El triángulo es equilátero")
        else:
            print("El triángulo no es equilátero")

#Principal
l1=int(input("lado1:"))
l2=int(input("lado2:"))
l3=int(input("lado3:"))
traingulo1=Triangulo(l1,l2,l3)
triangulo1.imprimir
triangulo2.imprimirMayor()
triangulo3.equilatero
