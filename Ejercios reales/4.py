import numpy as np

inventario = np.array([
    [25, 18, 30, 12],
    [15, 22, 17, 20],
    [32, 10, 24, 16]
])

productos = np.array(["Teclado", "Mouse", "Monitor", "Audífonos"])

print("Matriz de Inventario:\n", inventario)

print(f"\nTotal general de unidades: {np.sum(inventario)}")
totales_bodega = np.sum(inventario, axis=1)
for i, t in enumerate(totales_bodega, 1):
    print(f"Total Bodega {i}: {t}")

totales_producto = np.sum(inventario, axis=0)
for p, t in zip(productos, totales_producto):
    print(f"Total {p}: {t}")

idx_max = np.argmax(totales_producto)
idx_min = np.argmin(totales_producto)
print(f"\nProducto con mayor existencia: {productos[idx_max]} ({totales_producto[idx_max]} unidades)")
print(f"Producto con menor existencia: {productos[idx_min]} ({totales_producto[idx_min]} unidades)")

filtro_50 = totales_producto < 50
print(f"\nProductos con menos de 50 unidades: {list(productos[filtro_50])}")
