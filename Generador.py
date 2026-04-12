# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:13:08 2026

@author: ROG STRIX
"""

import tkinter as tk
from tkinter import messagebox
import pyodbc
import random

# 1. Configuración de la Ventana Principal
root = tk.Tk()
root.title("Generador Claves_Master")
root.geometry("400x350")

print("--- Iniciando aplicación ---")

def obtener_caracteres_db():
    print("Conectando a SQL Server...")
    try:
        server = r"DESKTOP-6IINT1V\SQLEXPRESS"
        conn_str = (
            f"Driver={{ODBC Driver 17 for SQL Server}};"
            f"Server={server};"
            f"Database=Claves_Master;"
            "Trusted_Connection=yes;"
        )
        conexion = pyodbc.connect(conn_str, timeout=5) # Timeout de 5 segundos
        cursor = conexion.cursor()
        cursor.execute("SELECT Contenido FROM ConfigGenerador")
        filas = cursor.fetchall()
        conexion.close()
        print("✅ Datos obtenidos de la DB")
        return "".join([f[0] for f in filas])
    except Exception as e:
        print(f"❌ Error en DB: {e}")
        return None

def ejecutar_generacion():
    pool = obtener_caracteres_db()
    if pool:
        try:
            longitud = int(entry_long.get())
            nueva_clave = "".join(random.choice(pool) for _ in range(longitud))
            txt_res.config(state="normal")
            txt_res.delete(0, tk.END)
            txt_res.insert(0, nueva_clave)
            txt_res.config(state="readonly")
        except ValueError:
            messagebox.showerror("Error", "La longitud debe ser un número")
    else:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos")

# --- Elementos Visuales ---
tk.Label(root, text="Longitud de Clave:", font=("Arial", 10)).pack(pady=10)
entry_long = tk.Entry(root, justify='center')
entry_long.insert(0, "12")
entry_long.pack()

tk.Button(root, text="Generar Clave Aleatoria", command=ejecutar_generacion, 
          bg="#2ecc71", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

txt_res = tk.Entry(root, font=("Consolas", 12), width=30, justify='center')
txt_res.pack(pady=10)
txt_res.config(state="readonly")

print("--- Ventana configurada, llamando a mainloop ---")

# VITAL: Forzar que la ventana aparezca al frente
root.lift()
root.attributes("-topmost", True)
root.after_idle(root.attributes, "-topmost", False)

root.mainloop()