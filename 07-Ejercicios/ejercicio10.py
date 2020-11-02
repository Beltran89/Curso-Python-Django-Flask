"""
Ejercicio 10: Pedir la nota de 15 alumnos y mostrar cuantos han aprobado y cuantos han suspendido

"""
apro=0
suspe=0

for alum in range(1,15 + 1):
    nota = int(input("Introduce nota alumno " + alum))
    if nota < 5:
        suspe = suspe + 1
    else:
        apro = apro + 1 

print(f"Total de aprobados {apro}, Total suspendidos {suspe}")