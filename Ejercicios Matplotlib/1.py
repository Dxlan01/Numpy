import matplotlib.pyplot as plt

fig, ax=plt.subplots()

producto=["pan", "leche", "arroz", "huvos"]
cantidad=[20, 15, 25, 30]

ax.plot(producto, cantidad)

ax.set_title("Ventas de productos")
ax.set_xlabel("Productos")
ax.set_ylabel("Cantidad vendidad")

plt.show()