import numpy as np

notas = np.array([
    [4.2, 3.8, 4.5, 4.0],
    [3.5, 2.9, 3.8, 3.2],
    [4.8, 4.6, 4.9, 4.7],
    [2.8, 3.1, 3.5, 3.0],
    [4.0, 4.2, 3.9, 4.4]
])

print(f"Promedio general: {np.mean(notas):.2f}")
print(f"Nota máxima: {np.max(notas)}")
print(f"Nota mínima: {np.min(notas)}")

promedios_aprendiz = np.mean(notas, axis=1)
promedios_evidencia = np.mean(notas, axis=0)
for i, p in enumerate(promedios_aprendiz, 1):
    print(f"Promedio Aprendiz {i}: {p:.2f}")
for i, p in enumerate(promedios_evidencia, 1):
    print(f"Promedio Evidencia {i}: {p:.2f}")
mejor_aprendiz = np.argmax(promedios_aprendiz) + 1
print(f"El aprendiz con mayor promedio es el Aprendiz {mejor_aprendiz}")
print(f"Cantidad de notas inferiores a 3.0: {np.sum(notas < 3.0)}")
print("\nAprendices con promedio >= 3.5:")
for i, p in enumerate(promedios_aprendiz, 1):
    if p >= 3.5:
        print(f"- Aprendiz {i} (Promedio: {p:.2f})")
