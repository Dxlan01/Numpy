import matplotlib.pyplot as plt

temperaturas = []
for i in range(1, 9):
    temp = float(input(f"Ingrese la temperatura de la hora {i} (°C): "))
    temperaturas.append(temp)

print(f"\nTemperaturas registradas: {temperaturas}")


promedio = sum(temperaturas) / len(temperaturas)
maxima = max(temperaturas)
minima = min(temperaturas)

print(f"Promedio: {promedio:.2f}°C")
print(f"Máxima: {maxima}°C")
print(f"Mínima: {minima}°C")


sobre_50 = [t for t in temperaturas if t > 50]
print(f"Temperaturas > 50°C: {len(sobre_50)}")


horas = [f"Hora {i}" for i in range(1, 9)]
plt.plot(horas, temperaturas, marker='o', color='b', label='Temperatura')
plt.axhline(y=50, color='r', linestyle='--', label='Límite Recomendado (50°C)') 

plt.title("Monitoreo de Temperatura del Servidor")
plt.xlabel("Horas")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.legend()
plt.show()
