# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:58:15 2026

@author: ROG STRIX
"""
import tkinter as tk
from tkinter import messagebox
import pyodbc
import os
import sys

# Configuración de tu SQL Server
SERVER = r"DESKTOP-6IINT1V\SQLEXPRESS"
DATABASE = "Claves_Master"
CONN_STR = f"Driver={{ODBC Driver 17 for SQL Server}};Server={SERVER};Database={DATABASE};Trusted_Connection=yes;"

def abrir_registro():
    """UNIDAD 4: Función para crear ventana secundaria (Toplevel)"""
    ventana_reg = tk.Toplevel(root)
    ventana_reg.title("Registro de Usuario")
    ventana_reg.geometry("300x400")
    ventana_reg.configure(bg="white")
    
    # Bloquea la ventana de atrás hasta que se cierre esta
    ventana_reg.grab_set()

    tk.Label(ventana_reg, text="CREAR NUEVA CUENTA", font=("Arial", 11, "bold"), bg="white", fg="#1a73e8").pack(pady=20)

    tk.Label(ventana_reg, text="Nombre de Usuario:", bg="white").pack()
    entry_n_user = tk.Entry(ventana_reg, font=("Arial", 10), bd=1, relief="solid")
    entry_n_user.pack(pady=5)

    tk.Label(ventana_reg, text="Nueva Contraseña:", bg="white").pack()
    entry_n_pass = tk.Entry(ventana_reg, font=("Arial", 10), show="*", bd=1, relief="solid")
    entry_n_pass.pack(pady=5)

    def guardar_usuario():
        """Lógica para insertar datos en SQL Server"""
        u = entry_n_user.get()
        p = entry_n_pass.get()

        # UNIDAD 3: Validación de campos vacíos
        if u == "" or p == "":
            messagebox.showwarning("Campos Requeridos", "Por favor, llena todos los campos.")
            return

        try:
            conn = pyodbc.connect(CONN_STR)
            cursor = conn.cursor()
            
            # UNIDAD 3: Verificar si el usuario ya existe
            cursor.execute("SELECT * FROM Usuarios WHERE Username = ?", (u,))
            if cursor.fetchone():
                messagebox.showwarning("Error", "Este usuario ya existe.")
            else:
                # UNIDAD 4: Inserción de datos
                cursor.execute("INSERT INTO Usuarios (Username, PasswordHash) VALUES (?, ?)", (u, p))
                conn.commit()
                messagebox.showinfo("Éxito", "Usuario creado con éxito. Ahora puedes iniciar sesión.")
                
                # CERRAMOS LA VENTANA DE REGISTRO PARA VOLVER AL LOGIN
                ventana_reg.destroy() 
                
            conn.close()
        except Exception as e:
            messagebox.showerror("Error de Base de Datos", str(e))

    tk.Button(ventana_reg, text="REGISTRARSE", command=guardar_usuario, 
              bg="#27ae60", fg="white", font=("Arial", 10, "bold"), width=15).pack(pady=25)

def ejecutar_login():
    """Lógica para validar acceso y entrar al Generador"""
    user = entry_usuario.get()
    psw = entry_password.get()
    
    try:
        conn = pyodbc.connect(CONN_STR)
        cursor = conn.cursor()
        # UNIDAD 3: Estructura de decisión para el Login
        cursor.execute("SELECT * FROM Usuarios WHERE Username = ? AND PasswordHash = ?", (user, psw))
        
        if cursor.fetchone():
            messagebox.showinfo("Acceso Garantizado", f"Bienvenido al sistema, {user}")
            root.destroy()
            # UNIDAD 4: Ejecución de archivo externo
            os.system(f'"{sys.executable}" Generador.py')
        else:
            messagebox.showwarning("Denegado", "Usuario o clave incorrectos.")
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", "Error al conectar con SQL Server.")

# --- INTERFAZ PRINCIPAL DE LOGIN ---
root = tk.Tk()
root.title("Claves_Master - Autenticación")
root.geometry("350x450")
root.configure(bg="#f8f9fa")

tk.Label(root, text="SISTEMA DE ACCESO", font=("Arial", 14, "bold"), bg="#f8f9fa", fg="#333").pack(pady=30)

# Campos de Entrada
tk.Label(root, text="Usuario:", bg="#f8f9fa").pack()
entry_usuario = tk.Entry(root, font=("Arial", 11), justify='center')
entry_usuario.pack(pady=5)

tk.Label(root, text="Contraseña:", bg="#f8f9fa").pack()
entry_password = tk.Entry(root, font=("Arial", 11), show="*", justify='center')
entry_password.pack(pady=5)

# Botón Principal
btn_login = tk.Button(root, text="INGRESAR", command=ejecutar_login, 
                      bg="#1a73e8", fg="white", width=22, font=("Arial", 10, "bold"))
btn_login.pack(pady=25)

# Enlace de Registro
tk.Label(root, text="¿No tienes una cuenta?", bg="#f8f9fa", font=("Arial", 9)).pack()
btn_link = tk.Button(root, text="Crea una cuenta aquí", command=abrir_registro, 
                     fg="#1a73e8", bg="#f8f9fa", bd=0, cursor="hand2", font=("Arial", 10, "underline"))
btn_link.pack()

root.mainloop()