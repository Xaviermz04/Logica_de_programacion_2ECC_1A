# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:58:15 2026

@author: ROG STRIX
"""
import tkinter as tk
from tkinter import messagebox
import pyodbc

def validar_login():
    usuario_ingresado = entry_usuario.get()
    clave_ingresada = entry_password.get()

    # 1. Configuración de conexión (Ajustada a tu servidor verificado)
    # Usamos 'r' al inicio para evitar el SyntaxWarning por la barra invertida
    server_name = r"DESKTOP-6IINT1V\SQLEXPRESS" 
    db_name = "Claves_Master"
    
    # Usaremos el Driver 17 que vimos en tu lista, es muy estable
    conn_str = (
        f"Driver={{ODBC Driver 17 for SQL Server}};"
        f"Server={server_name};"
        f"Database={db_name};"
        "Trusted_Connection=yes;"
    )

    try:
        conexion = pyodbc.connect(conn_str)
        cursor = conexion.cursor()

        # 2. Consulta a la tabla 'Usuarios'
        query = "SELECT * FROM Usuarios WHERE Username = ? AND PasswordHash = ?"
        cursor.execute(query, (usuario_ingresado, clave_ingresada))
        
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo("Acceso Concedido", f"¡Bienvenido al sistema, {usuario_ingresado}!")
            # ventana.destroy() # Podrías cerrar el login y abrir el menú principal aquí
        else:
            messagebox.showwarning("Acceso Denegado", "Usuario o contraseña incorrectos.")

        conexion.close()

    except Exception as e:
        messagebox.showerror("Error de Base de Datos", f"No se pudo consultar la base: {e}")

# --- Interfaz Gráfica con Tkinter ---

app = tk.Tk()
app.title("Sistema Claves_Master")
app.geometry("350x300")
app.configure(bg="#f0f0f0")

# Contenedor principal
frame = tk.Frame(app, bg="#f0f0f0")
frame.pack(expand=True)

# Título
tk.Label(frame, text="INICIO DE SESIÓN", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=20)

# Campos de entrada
tk.Label(frame, text="Usuario", bg="#f0f0f0").pack()
entry_usuario = tk.Entry(frame, width=25, font=("Arial", 11))
entry_usuario.pack(pady=5)

tk.Label(frame, text="Contraseña", bg="#f0f0f0").pack()
entry_password = tk.Entry(frame, width=25, font=("Arial", 11), show="*")
entry_password.pack(pady=5)

# Botón con un poco de estilo
btn_login = tk.Button(frame, text="Ingresar", command=validar_login, 
                      bg="#0078d4", fg="white", width=15, font=("Arial", 10, "bold"))
btn_login.pack(pady=30)

app.mainloop()