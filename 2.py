import numpy as np
# Calificaciones de un grupo de estudiantes en un examen
calificaciones = np.array([4.5, 2.8, 3.9, 5.0, 3.0, 1.5, 4.2])
# Queremos saber quiénes aprobaron (calificación mayor o igual a 3.0)
# NumPy revisa todo el arreglo y crea una lista solo con los aprobados
aprobados = calificaciones[calificaciones >= 3.0]
print("Todas las notas:", calificaciones)
print("Notas aprobadas:", aprobados)