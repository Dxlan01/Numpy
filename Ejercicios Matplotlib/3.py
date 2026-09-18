import matplotlib.pyplot as plt

dias =["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
ventas=[20, 35, 25, 40, 30]

plt.bar(dias, ventas)

plt.title("ventas de la semana")
plt.xlabel("Dias")
plt.ylabel("Ventas")

plt.show()