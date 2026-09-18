import matplotlib.pyplot as plt

fig, ax=plt.subplots(2, 2)

ax[0, 0].plot([1, 2, 3], [10, 20, 15])
ax[0, 0].set_title("Grafico 1")

ax[0, 1].plot(["A", "B", "C"], [10, 20, 15])
ax[0, 1].set_title("Grafico 2")

ax[1, 0].plot([1, 2, 3], [5, 15, 10])
ax[1, 0].set_title("Grafico 3")

ax[1, 1].plot(["X", "Y", "Z"], [20, 10, 30])
ax[1, 1].set_title("Grafico 4")

plt.show()