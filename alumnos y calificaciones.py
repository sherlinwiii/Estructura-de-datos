import random
import time

class Escuela:
    def __init__(self, num_alumnos, num_materias):
        self.num_alumnos = num_alumnos
        self.num_materias = num_materias
        self.matriz = [[random.randint(0, 100) for _ in range(num_materias)] for _ in range(num_alumnos)]

    def buscar_calificacion(self, alumno, materia):
        if 1 <= alumno <= self.num_alumnos and 1 <= materia <= self.num_materias:
            return self.matriz[alumno - 1][materia - 1]
        else:
            return None  

    def mostrar_tabla(self):
        print("\nTabla de calificaciones:")
        
     
        encabezado = ["Alumno"] + [f"Materia {i+1}" for i in range(self.num_materias)]
        print(f"{encabezado[0]:<10} " + " ".join(f"{m:<10}" for m in encabezado[1:]))
        print("-" * (10 + self.num_materias * 10))

        for i in range(self.num_alumnos):
            fila = [f"{i+1:<10}"] + [f"{self.matriz[i][j]:<10}" for j in range(self.num_materias)]
            print(" ".join(fila))


num_alumnos = int(input("Ingrese el número de alumnos: "))
num_materias = int(input("Ingrese el número de materias: "))


inicio = time.time()

escuela = Escuela(num_alumnos, num_materias)

escuela.mostrar_tabla()

alumno_buscar = int(input("\nIngrese el número de alumno a buscar: "))
materia_buscar = int(input("Ingrese el número de materia a buscar: "))

calificacion = escuela.buscar_calificacion(alumno_buscar, materia_buscar)
if calificacion is not None:
    print(f"\n La calificación del Alumno {alumno_buscar} en la Materia {materia_buscar} es: {calificacion}")
else:
    print("\n Error: El número de alumno o materia está fuera de rango.")


fin = time.time()
print(f"\n Tiempo de ejecución: {fin - inicio:.5f} segundos")
