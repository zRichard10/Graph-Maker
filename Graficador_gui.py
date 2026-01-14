import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt

def graficar():
    try:
        x_raw = entrada_x.get().replace(" ", "")
        y_raw = entrada_y.get().replace(" ", "")
        x_vals = list(map(float, x_raw.split(',')))
        y_vals = list(map(float, y_raw.split(',')))

        if len(x_vals) != len(y_vals):
            raise ValueError("Cantidad distinta de elementos")

        plt.figure()
        plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='blue')
        plt.title("Gráfica Personalizada")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.grid(True)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.show()

    except:
        messagebox.showerror("Error", "Ingresa números válidos separados por comas. (ej: -4,-2,0,2,4)")

def limpiar():
    entrada_x.delete(0, tk.END)
    entrada_y.delete(0, tk.END)

def guardar_imagen():
    try:
        x_raw = entrada_x.get().replace(" ", "")
        y_raw = entrada_y.get().replace(" ", "")
        x_vals = list(map(float, x_raw.split(',')))
        y_vals = list(map(float, y_raw.split(',')))

        if len(x_vals) != len(y_vals):
            raise ValueError("Cantidad distinta de elementos")

        ruta = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Imagen PNG", "*.png")])
        if ruta:
            plt.figure()
            plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='blue')
            plt.title("Gráfica Personalizada")
            plt.xlabel("Eje X")
            plt.ylabel("Eje Y")
            plt.grid(True)
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.savefig(ruta)
            messagebox.showinfo("Guardado", f"Gráfica guardada como:\n{ruta}")
    except:
        messagebox.showerror("Error", "No se pudo guardar. Verifica los datos y vuelve a intentarlo.")

# Ventana principal
ventana = tk.Tk()
ventana.title("MiniGraficador v2")
ventana.geometry("450x250")
ventana.resizable(False, False)

# Campos
tk.Label(ventana, text="Valores de X (separados por coma):").pack(pady=5)
entrada_x = tk.Entry(ventana, width=50)
entrada_x.pack()

tk.Label(ventana, text="Valores de Y (separados por coma):").pack(pady=5)
entrada_y = tk.Entry(ventana, width=50)
entrada_y.pack()

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=15)

tk.Button(frame_botones, text="Graficar", command=graficar, bg="lightblue", width=12).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Guardar Imagen", command=guardar_imagen, bg="lightgreen", width=15).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Limpiar", command=limpiar, bg="lightcoral", width=12).grid(row=0, column=2, padx=5)

ventana.mainloop()
