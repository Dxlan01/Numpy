import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 3, 5, 4, 6, 8]

plt.plot(x, y, color='green', linewidth=2, marker='o')
plt.title('Ejemplo básico de línea', color='black')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.3)
plt.show()