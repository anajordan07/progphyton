#leer un empleado
def cargaEmpleado():
    nombre=input("Introduce una nombre:")
    sueldo=int(input("Intoduce el sueldo:"))
    return(nombre,sueldo)
    

#Visualizar el mayor sueldo de dos empleados
def mayorsueldo(empleado1,sueldo2):
    if(empleado1[1]>empleado2[1]):
        print("EL mayor sueldo lo tiene", empleado1[0],"con",empleado1[1])
    else:
       print("EL mayor sueldo lo tiene", empleado2[0],"con",empleado2[1])
        
#Programa principal
empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)
