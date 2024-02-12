#agregar estudiante
def agregar(lista):
    codigo=int(input("Codigo:"))
    nombreYapel=input("Nombre y Apellidos:")
    asignatura=input("Asignatura:")
    nota=float(input("Nota:"))
    lista.append((codigo,nombreYapel,asignatura,nota))
    return lista
#eliminar estudiante por codigo
def eliminar(lista,codigo):
    indice=0
    estado=1
    while estado==1 and indice<len(lista):
        esstudiante=lista[indice]
        if estudiante[0]==codigo:
            estado=0
            indice=indice+1
#Modificar estudiante
def modificar(lista,codigo):
    indice=0
    estado=1
    while estado==1 and indice<len(lista):
        estudiantes=lista[indice]
        if estudiante [0]==codigo:
            nombreYapel=input("Nuevo Nombre y apellido")
            asignatura=input("nueva asignatura:")
            nota=float(input("nueva nota:"))
            estado=0
        indice=indice+1
    if estado==0:
        lista.pop(indice-1)
        lista.insert(indice-1,(codigo,nombreYapel,asignatura,nota))
    return lista

#Mostrar todos los estudiantes
def mostrarPorAsignatura(lista,asignatura):
    for estudiante in lista:
        if estudiante[2]=asignatura::
            for datos in estudiante:
                print(datos,end=" ")
            print()
#Mostrar aprobados por asignatura
            def mostrarAprobadosPorAsignatura(lista,asignatura):
                for estudiante in lista:
                    if estudiante [2]==asignatura:
                        for datos in estudiante:
                            print(datos,end" ")
                        print()
#Menu
def menu():
    print("1.Agregar estudiante")
    print("2.Eliminar un estudiantes(por codigo)")
    print("3.Modificar el nuevo estudiante")
    print("4.Mostrar todos los estudiantes")
    print("5.Mostrar estudiante por asignatura")
    print("6.Mostrasçr aprobados por asignatura")
    print("7.salir")
    opcion=int(input("elige una opcion"))
    return opcion
#Principal
op=0
lista=[]
while op!=7:
    op=menu()
    if op==1:
       lista=agregar(lista)
    if op==2:
        codigo=int(input("COdigo a eliminar:"))
    if op==3:
        codigo=int(input("Codigo a modificar"))
        lista=modificar(lista,codigo)
    if op==4:
        mostrarTodos(lista)
    if op==5:
        asignatura=input("Asignatura a consultar:")
        mostrarPorAsignatura(lista,asignatura)
    if op==6
        asignatura=input("Asignatura a consultar:")
        mostrarAprobadosPorAsignatura(lista,asignatura)
