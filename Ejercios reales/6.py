import tkinter as tk
from tkinter import messagebox

estudiantes = []

def registrar():
    nombre = entry_nombre.get().strip()
    edad = entry_edad.get().strip()
    programa = entry_programa.get().strip()
    
    if not nombre or not edad or not programa:
        messagebox.showwarning("Atención", "Todos los campos son obligatorios")
        return
        
    estudiantes.append({"nombre": nombre, "edad": edad, "programa": programa})
    
    lbl_info.config(text=f"Registrado:\nNombre: {nombre}\nEdad: {edad}\nPrograma: {programa}")
    limpiar()

def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_programa.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Registro de Estudiantes")
ventana.geometry("350x320")

tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Programa de Formación:").pack()
entry_programa = tk.Entry(ventana)
entry_programa.pack()

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_registrar = tk.Button(frame_botones, text="Registrar", command=registrar)
btn_registrar.pack(side=tk.LEFT, padx=5)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar)
btn_limpiar.pack(side=tk.LEFT, padx=5)

lbl_info = tk.Label(ventana, text="", fg="blue", justify=tk.LEFT)
lbl_info.pack(pady=10)

ventana.mainloop()
