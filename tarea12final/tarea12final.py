import os

class Alumno:
    def __init__(self, codigo, nombre, apellidos, nota):
        self.codigo = codigo
        self.nombre = nombre
        self.apellidos = apellidos
        self.nota = nota

class InterfazNotas:
    def __init__(self):
        self.alumnos = []

    def alta_alumno(self):
        codigo = input("Introduce el código del alumno: ")
        nombre = input("Introduce el nombre del alumno: ")
        apellidos = input("Introduce los apellidos del alumno: ")
        nota = float(input("Introduce la nota del alumno: "))
        alumno = Alumno(codigo, nombre, apellidos, nota)
        self.alumnos.append(alumno)
        print("Alumno registrado correctamente.")

    def consulta_aprobados(self):
        aprobados = [alumno for alumno in self.alumnos if alumno.nota >= 5.0]
        self._mostrar_alumnos(aprobados)

    def consulta_suspendidos(self):
        suspendidos = [alumno for alumno in self.alumnos if alumno.nota < 5.0]
        self._mostrar_alumnos(suspendidos)

    def _mostrar_alumnos(self, lista_alumnos):
        if not lista_alumnos:
            print("No hay alumnos para mostrar.")
        else:
            for alumno in lista_alumnos:
                print(f"Código: {alumno.codigo}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, Nota: {alumno.nota}")

    def generar_informe(self, filename):
        with open(filename, 'w') as file:
            file.write("Listado de Alumnos:\n")
            for alumno in self.alumnos:
                file.write(f"Código: {alumno.codigo}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, Nota: {alumno.nota}\n")

    def ejecutar(self):
        while True:
            print("\nBienvenido al sistema de control de notas de alumnos:")
            print("1. Alta de alumno")
            print("2. Consulta de alumnos aprobados")
            print("3. Consulta de alumnos suspendidos")
            print("4. Generar informe en fichero")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.alta_alumno()
            elif opcion == '2':
                self.consulta_aprobados()
            elif opcion == '3':
                self.consulta_suspendidos()
            elif opcion == '4':
                filename = input("Introduce el nombre del archivo para el informe: ")
                self.generar_informe(filename)
                print(f"Informe generado en {filename}.")
            elif opcion == '5':
                print("Gracias por utilizar el sistema. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    interfaz = InterfazNotas()
    interfaz.ejecutar()
