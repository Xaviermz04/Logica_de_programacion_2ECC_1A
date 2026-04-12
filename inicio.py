# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:58:15 2026

@author: ROG STRIX
"""
import tkinter as tk
from tkinter import messagebox

def validar_login():
    usuario = entry_usuario.get()
    password = entry_password.get()

    # Validación simple (puedes cambiar esto por una base de datos)
    if usuario == "admin" and password == "1234":
        messagebox.showinfo("Éxito", f"Bienvenido, {usuario}")
        ventana.destroy() # Cierra la ventana al entrar
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# 1. Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("300x200")

# 2. Etiquetas y campos de entrada (Labels y Entrys)
tk.Label(ventana, text="Usuario:").pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

tk.Label(ventana, text="Contraseña:").pack(pady=5)
entry_password = tk.Entry(ventana, show="*") # Muestra asteriscos en lugar de letras
entry_password.pack(pady=5)

# 3. Botón de acceso
boton_login = tk.Button(ventana, text="Entrar", command=validar_login)
boton_login.pack(pady=20)

# 4. Ejecutar el bucle de la aplicación
ventana.mainloop()