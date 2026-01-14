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
            raise ValueError("Different number of elements.")

        plt.figure()
        plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='blue')
        plt.title("Graph Maker")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.show()

    except:
        messagebox.showerror("Error", "Enter valid numbers separated by commas. (e.g., -4, -2, 0, 2, 4")

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
            raise ValueError("Different number of elements.")

        ruta = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Imagen PNG", "*.png")])
        if ruta:
            plt.figure()
            plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='blue')
            plt.title("Graph Maker")
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.grid(True)
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.savefig(ruta)
            messagebox.showinfo("Saved", f"Graph save as:\n{ruta}")
    except:
        messagebox.showerror("Error", "Save failed. Please check your data and try again")

# Main window
ventana = tk.Tk()
ventana.title("Graph Maker v2")
ventana.geometry("450x250")
ventana.resizable(False, False)

# Fields
tk.Label(ventana, text="X values (comma-separated):").pack(pady=5)
entrada_x = tk.Entry(ventana, width=50)
entrada_x.pack()

tk.Label(ventana, text="Y values (comma-separated):").pack(pady=5)
entrada_y = tk.Entry(ventana, width=50)
entrada_y.pack()

# Buttons
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=15)

tk.Button(frame_botones, text="To Graph", command=graficar, bg="lightblue", width=12).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Save Image", command=guardar_imagen, bg="lightgreen", width=15).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Clear", command=limpiar, bg="lightcoral", width=12).grid(row=0, column=2, padx=5)

ventana.mainloop()

