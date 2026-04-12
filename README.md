# Logica\_de\_programacion\_2ECC\_1A

Repositorio creado con fin educativo



Aquí tienes el formato listo para que lo selecciones, copies y pegues directamente en el Bloc de notas. He organizado la información de manera limpia para que se vea profesional como documentación técnica.



Plaintext

============================================================

&#x20;               PROYECTO: CLAVES\_MASTER

============================================================



DESCRIPCIÓN GENERAL:

Sistema de gestión y generación de contraseñas seguras 

integrado con SQL Server 2022. Estructura modular con 

validación de acceso y herramientas de generación dinámica.



\------------------------------------------------------------

ESPECIFICACIONES TÉCNICAS:

\------------------------------------------------------------

\* Lenguaje: Python 3.13.x

\* Base de Datos: Microsoft SQL Server 2022 (Express Edition)

\* Interfaz Gráfica: Tkinter

\* Entorno: Spyder IDE



\------------------------------------------------------------

LIBRERÍAS Y VERSIONES:

\------------------------------------------------------------

1\. pyodbc (v5.3.0+): 

&#x20;  Conexión entre Python y SQL Server vía ODBC.

&#x20;  

2\. tkinter (Integrada): 

&#x20;  Desarrollo de ventanas de Login y Generador.

&#x20;  

3\. random (Integrada): 

&#x20;  Lógica de generación aleatoria de caracteres.

&#x20;  

4\. os / sys (Integrada): 

&#x20;  Gestión de archivos (inicio.py y Generador.py).

&#x20;  

5\. spyder-kernels (v3.1.x): 

&#x20;  Compatibilidad del intérprete en Spyder.



\------------------------------------------------------------

FUNCIONALIDADES PRINCIPALES:

\------------------------------------------------------------

\* LOGIN: Validación de usuarios en la tabla \[Usuarios].

\* DB CONFIG: Caracteres cargados desde \[ConfigGenerador].

\* BARRA DE LONGITUD: Límite físico máximo de 16 caracteres.

\* PORTAPAPELES: Botón para copiar clave instantáneamente.

\* CIERRE DE SESIÓN: Retorno seguro a la pantalla de inicio.



\------------------------------------------------------------

REQUISITOS DE INSTALACIÓN:

\------------------------------------------------------------

1\. Instalar ODBC Driver 17 for SQL Server.

2\. Ejecutar en terminal:

&#x20;  pip install pyodbc spyder-kernels==3.1.\*



============================================================

Desarrollado por: Jose Xavier Menendez Zambrano

Fecha: 12 de Abril, 2026

============================================================

