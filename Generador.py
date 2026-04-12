# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:13:08 2026

@author: ROG STRIX
"""
import tkinter as tk
from tkinter import messagebox
import pyodbc
import random
import os
import sys

def obtener_caracteres_db():
    try:
        server = r"DESKTOP-6IINT1V\SQLEXPRESS"
        conn_str = f"Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database=Claves_Master;Trusted_Connection=yes;"
        conexion = pyodbc.connect(conn_str)
        cursor = conexion.cursor()
        cursor.execute("SELECT Contenido FROM ConfigGenerador")
        filas = cursor.fetchall()
        conexion.close()
        return "".join([f[0] for f in filas])
    except Exception:
        return None

def ejecutar_generacion():
    pool = obtener_caracteres_db()
    if pool:
        # Ahora obtenemos la longitud desde la barra (Scale)
        longitud = barra_longitud.get()
        nueva_clave = "".join(random.choice(pool) for _ in range(longitud))
        
        txt_res.config(state="normal")
        txt_res.delete(0, tk.END)
        txt_res.insert(0, nueva_clave)
        txt_res.config(state="readonly")
    else:
        messagebox.showerror("Error", "No se pudo conectar con la base de datos.")

def copiar_clave():
    clave = txt_res.get()
    if clave:
        root.clipboard_clear()
        root.clipboard_append(clave)
        messagebox.showinfo("Copiado", "Clave copiada al portapapeles")
    else:
        messagebox.showwarning("Aviso", "Primero genera una clave")

def cerrar_sesion():
    if messagebox.askyesno("Cerrar Sesión", "¿Deseas regresar al login?"):
        root.destroy()
        # Lanza de nuevo el archivo de inicio
        os.system(f'"{sys.executable}" inicio.py')

# --- Interfaz Gráfica ---
root = tk.Tk()
root.title("Generador Claves_Master")
root.geometry("400x450")
root.configure(bg="#f4f4f4")

tk.Label(root, text="GENERADOR SEGURO", font=("Arial", 12, "bold"), bg="#f4f4f4").pack(pady=15)

# 1. Validación con Barra (Scale) hasta 16
tk.Label(root, text="Longitud de la clave (Máx 16):", bg="#f4f4f4").pack()
barra_longitud = tk.Scale(root, from_=4, to=16, orient=tk.HORIZONTAL, length=200, bg="#f4f4f4")
barra_longitud.set(12) # Valor inicial
barra_longitud.pack(pady=10)

btn_gen = tk.Button(root, text="Generar Clave ⚡", command=ejecutar_generacion, 
                    bg="#27ae60", fg="white", width=20, font=("Arial", 10, "bold"))
btn_gen.pack(pady=10)

txt_res = tk.Entry(root, font=("Consolas", 12), width=25, justify='center')
txt_res.pack(pady=10)
txt_res.config(state="readonly")

# 2. Botón de Copiar
btn_copiar = tk.Button(root, text="Copiar al Portapapeles 📋", command=copiar_clave, 
                       bg="#f39c12", fg="white", width=20)
btn_copiar.pack(pady=5)

# 3. Botón de Cerrar Sesión
btn_logout = tk.Button(root, text="Cerrar Sesión 🚪", command=cerrar_sesion, 
                       bg="#c0392b", fg="white", width=20)
btn_logout.pack(pady=30)

root.mainloop()