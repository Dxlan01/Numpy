import numpy as np
calificaciones = np.array([4.5, 2.8, 3.9, 5.0, 3.0, 1.5, 4.2])
aprobados = calificaciones[calificaciones >= 3.0]
print("Todas las notas:", calificaciones)
print("Notas aprobadas:", aprobados)