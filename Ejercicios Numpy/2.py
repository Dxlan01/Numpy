import numpy as np

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota5 = float(input("Ingrese la nota 5: "))

notas = np.array([nota1, nota2, nota3, nota4, nota5])

suma = np.sum(notas)
promedio = np.mean(notas)
mayor = np.max(notas)
menor = np.min(notas)

aprobadas = np.sum(notas >= 3)

print("\n--- RESULTADOS ---")
print("Notas:", notas)
print("Suma:", suma)
print("Promedio:", promedio)
print("Nota mayor:", mayor)
print("Nota menor:", menor)
print("Notas aprobadas:", aprobadas)