import tkinter as tk

def calcular():
    masa = float(caja1.get())
    aceleracion = float(caja2.get())

    fuerza = masa * aceleracion

    resultado.config(text="Fuerza = " + str(fuerza) + " N")


ventana = tk.Tk()

tk.Label(ventana, text="Masa (kg)").pack()
caja1 = tk.Entry(ventana)
caja1.pack()

tk.Label(ventana, text="Aceleración (m/s²)").pack()
caja2 = tk.Entry(ventana)
caja2.pack()

tk.Button(ventana, text="Calcular", command=calcular).pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()