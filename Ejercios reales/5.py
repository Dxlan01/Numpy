import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        n3 = float(entry3.get())
        
        promedio = (n1 + n2 + n3) / 3
        estado = "Aprobado" if promedio >= 3.0 else "No aprobado"
        
        lbl_resultado.config(text=f"Promedio: {promedio:.2f} - {estado}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")()
def limpiar():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    lbl_resultado.config(text="")()
ventana = tk.Tk()
ventana.title("Calculadora de Promedio")
ventana.geometry("300x250")

tk.Label(ventana, text="Nota 1:").pack()
entry1 = tk.Entry(ventana)
entry1.pack()

tk.Label(ventana, text="Nota 2:").pack()
entry2 = tk.Entry(ventana)
entry2.pack()

tk.Label(ventana, text="Nota 3:").pack()
entry3 = tk.Entry(ventana)
entry3.pack()

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
btn_calcular.pack(pady=5)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
btn_limpiar.pack()

lbl_resultado = tk.Label(ventana, text="", font=("Arial", 11, "bold"))
lbl_resultado.pack(pady=10)

ventana.mainloop()