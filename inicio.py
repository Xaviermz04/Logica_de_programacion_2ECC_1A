# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:58:15 2026

@author: ROG STRIX
"""
import tkinter as tk
from tkinter import messagebox
import pyodbc
import os # Para ejecutar comandos del sistema
import sys # Para saber qué ejecutable de Python usar

def ejecutar_login():
    usuario = entry_usuario.get()
    password = entry_password.get()

    # Datos de tu servidor verificado
    server = r"DESKTOP-6IINT1V\SQLEXPRESS"
    db = "Claves_Master"
    conn_str = f"Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database={db};Trusted_Connection=yes;"

    try:
        conexion = pyodbc.connect(conn_str)
        cursor = conexion.cursor()
        
        # Validación en la base de datos
        query = "SELECT * FROM Usuarios WHERE Username = ? AND PasswordHash = ?"
        cursor.execute(query, (usuario, password))
        resultado = cursor.fetchone()
        
        conexion.close()

        if resultado:
            messagebox.showinfo("Éxito", "Acceso correcto. Abriendo generador...")
            
            # 1. Cerramos la ventana actual de login
            root.destroy()
            
            # 2. Abrimos el archivo Generador.py usando el mismo Python de Spyder
            # sys.executable asegura que use el Python donde instalaste pyodbc
            os.system(f'"{sys.executable}" Generador.py')
            
        else:
            messagebox.showwarning("Denegado", "Usuario o clave incorrectos")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar: {e}")

# --- Interfaz de Login ---
root = tk.Tk()
root.title("Login Claves_Master")
root.geometry("300x250")

tk.Label(root, text="USUARIO").pack(pady=10)
entry_usuario = tk.Entry(root)
entry_usuario.pack()

tk.Label(root, text="CONTRASEÑA").pack(pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Entrar", command=ejecutar_login, bg="#0078d4", fg="white").pack(pady=20)

root.mainloop()