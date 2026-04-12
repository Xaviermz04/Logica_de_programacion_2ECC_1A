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
    """
    FUNCIONALIDAD COMPLEJA: Conexión y Extracción de Datos.
    Se utiliza una estructura lógica 'try-except' para manejar errores de red o base de datos.
    """
    try:
        server = r"DESKTOP-6IINT1V\SQLEXPRESS"
        conn_str = f"Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database=Claves_Master;Trusted_Connection=yes;"
        
        conexion = pyodbc.connect(conn_str, timeout=5)
        cursor = conexion.cursor()
        
        # Consulta SQL para traer los sets de caracteres configurados
        cursor.execute("SELECT Contenido FROM ConfigGenerador")
        filas = cursor.fetchall()
        conexion.close()
        
        # ESTRUCTURA REPETITIVA: Comprensión de lista para unir los resultados
        return "".join([f[0] for f in filas])
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

def ejecutar_generacion():
    """
    ESTRUCTURA LÓGICA PRINCIPAL: 
    Valida la disponibilidad de la DB antes de proceder con la aleatoriedad.
    """
    pool_caracteres = obtener_caracteres_db()
    
    # Estructura Lógica: Si no hay conexión, se detiene el proceso
    if not pool_caracteres:
        messagebox.showerror("Error de Sistema", "No se pudo acceder a la configuración de caracteres en SQL Server.")
        return

    try:
        longitud = barra_longitud.get()
        password_final = ""
        
        # ESTRUCTURA REPETITIVA: Bucle 'for' para construir la clave carácter por carácter
        # Se repite tantas veces como la longitud seleccionada en la barra
        for i in range(longitud):
            caracter_azar = random.choice(pool_caracteres)
            password_final += caracter_azar
        
        # Actualización de la interfaz
        txt_res.config(state="normal")
        txt_res.delete(0, tk.END)
        txt_res.insert(0, password_final)
        txt_res.config(state="readonly")
        
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un fallo en la lógica de generación: {e}")

def copiar_clave():
    clave = txt_res.get()
    # Estructura Lógica: Verifica que el campo no esté vacío antes de copiar
    if clave:
        root.clipboard_clear()
        root.clipboard_append(clave)
        messagebox.showinfo("Copiado", "La clave ha sido enviada al portapapeles.")
    else:
        messagebox.showwarning("Aviso", "No hay ninguna clave generada para copiar.")

def cerrar_sesion():
    # Estructura Lógica: Ventana de confirmación (Sí/No)
    if messagebox.askyesno("Confirmación", "¿Está seguro de que desea cerrar la sesión actual?"):
        root.destroy()
        # Lógica de sistema para reiniciar el flujo del programa
        os.system(f'"{sys.executable}" inicio.py')

# --- Construcción de la Interfaz (Tkinter) ---
root = tk.Tk()
root.title("Generador Claves_Master - v2.0")
root.geometry("400x450")
root.configure(bg="#f0f2f5")

# Título 
tk.Label(root, text="SISTEMA DE GENERACIÓN DINÁMICA", font=("Segoe UI", 12, "bold"), 
         bg="#f0f2f5", fg="#1a73e8").pack(pady=20)

# Componente de Barra (Scale) - Implementa la validación física de longitud
tk.Label(root, text="Seleccione la longitud (Máx 16):", bg="#f0f2f5").pack()
barra_longitud = tk.Scale(root, from_=4, to=16, orient=tk.HORIZONTAL, length=250, 
                          bg="#f0f2f5", highlightthickness=0)
barra_longitud.set(12) 
barra_longitud.pack(pady=10)

# Botones de Acción
btn_gen = tk.Button(root, text="GENERAR", command=ejecutar_generacion, 
                    bg="#1a73e8", fg="white", width=25, font=("Segoe UI", 9, "bold"))
btn_gen.pack(pady=10)

txt_res = tk.Entry(root, font=("Consolas", 14), width=22, justify='center', 
                   bd=2, relief="flat")
txt_res.pack(pady=15)
txt_res.config(state="readonly")

btn_copiar = tk.Button(root, text="Copiar Clave", command=copiar_clave, 
                       bg="#34a853", fg="white", width=20)
btn_copiar.pack(pady=5)

btn_logout = tk.Button(root, text="Cerrar Sesión", command=cerrar_sesion, 
                       bg="#ea4335", fg="white", width=20)
btn_logout.pack(pady=25)

root.mainloop()