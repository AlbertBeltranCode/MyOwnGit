import tkinter as tk
from tkinter import filedialog, messagebox
from init_repo import init_repo
from staging import agregar_a_staging
from remove_staging import remover_de_staging
from commit import hacer_commit
from history import mostrar_historial
import os

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Repositorios")
ventana.geometry("400x300")

# Variable global para almacenar la ruta del archivo seleccionado
ruta_archivo_seleccionado = ""

# Función para seleccionar archivo
def seleccionar_archivo():
    global ruta_archivo_seleccionado
    ruta_archivo_seleccionado = filedialog.askopenfilename(title="Seleccionar archivo")
    if ruta_archivo_seleccionado:
        etiqueta_archivo_seleccionado.config(text=f"Archivo seleccionado: {os.path.basename(ruta_archivo_seleccionado)}")
    else:
        etiqueta_archivo_seleccionado.config(text="No se seleccionó ningún archivo")

# Creamos las funciones que se llamarán al presionar los botones
def ejecutar_init_repo():
    nombre_repo = "mi_repositorio"
    init_repo(nombre_repo)

def ejecutar_agregar_a_staging():
    if ruta_archivo_seleccionado:
        nombre_repo = "mi_repositorio"
        agregar_a_staging(nombre_repo, ruta_archivo_seleccionado)
    else:
        messagebox.showerror("Error", "Por favor selecciona un archivo primero.")

def ejecutar_remover_de_staging():
    if ruta_archivo_seleccionado:
        nombre_repo = "mi_repositorio"
        remover_de_staging(nombre_repo, ruta_archivo_seleccionado)
    else:
        messagebox.showerror("Error", "Por favor selecciona un archivo primero.")

def ejecutar_hacer_commit():
    if ruta_archivo_seleccionado:
        nombre_repo = "mi_repositorio"
        mensaje_commit = entrada_mensaje.get()
        if mensaje_commit:
            hacer_commit(nombre_repo, ruta_archivo_seleccionado, mensaje_commit)
        else:
            messagebox.showerror("Error", "Por favor ingresa un mensaje de commit.")
    else:
        messagebox.showerror("Error", "Por favor selecciona un archivo primero.")

def ejecutar_mostrar_historial():
    nombre_repo = "mi_repositorio"
    mostrar_historial(nombre_repo)

# Creamos los elementos de la interfaz
boton_init_repo = tk.Button(ventana, text="Inicializar Repositorio", command=ejecutar_init_repo)
boton_init_repo.pack(pady=10)

# Botón para seleccionar el archivo
boton_seleccionar_archivo = tk.Button(ventana, text="Seleccionar Archivo", command=seleccionar_archivo)
boton_seleccionar_archivo.pack(pady=5)

# Etiqueta para mostrar el archivo seleccionado
etiqueta_archivo_seleccionado = tk.Label(ventana, text="No se seleccionó ningún archivo")
etiqueta_archivo_seleccionado.pack(pady=5)

# Entrada para el mensaje del commit
etiqueta_mensaje = tk.Label(ventana, text="Mensaje del commit:")
etiqueta_mensaje.pack()

entrada_mensaje = tk.Entry(ventana)
entrada_mensaje.pack()

# Botones para las diferentes funciones
boton_agregar_staging = tk.Button(ventana, text="Agregar a Staging", command=ejecutar_agregar_a_staging)
boton_agregar_staging.pack(pady=5)

boton_remover_staging = tk.Button(ventana, text="Remover de Staging", command=ejecutar_remover_de_staging)
boton_remover_staging.pack(pady=5)

boton_hacer_commit = tk.Button(ventana, text="Hacer Commit", command=ejecutar_hacer_commit)
boton_hacer_commit.pack(pady=10)

boton_mostrar_historial = tk.Button(ventana, text="Mostrar Historial", command=ejecutar_mostrar_historial)
boton_mostrar_historial.pack(pady=10)

# Ejecutamos el loop
ventana.mainloop()
