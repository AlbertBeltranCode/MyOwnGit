import os
import time

#Declaramos una funcion make_commit para crear los commits dentro de la carpeta .git
def hacer_commit(nombre_repo, nombre_archivo, mensaje_commit):
    directorio_git = os.path.join(nombre_repo, ".git")
    archivo_commit = os.path.join(directorio_git, 'commits.txt')  # Archivo donde guardas los commits
    
    if os.path.exists(directorio_git) and os.path.exists(os.path.join(nombre_repo, nombre_archivo)):
        # Leemos el contenido del archivo que se va a hacer commit
        with open(os.path.join(nombre_repo, nombre_archivo), 'r') as f:
            contenido_archivo = f.read()

        # Obtenemos la hora del commit
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        
        # Guardamos el commit en el archivo commits.txt dentro de la carpeta ".git"
        with open(archivo_commit, 'a') as f:
            f.write(f"Commit: {mensaje_commit}\n")
            f.write(f"Date: {timestamp}\n")
            f.write(f"File: {nombre_archivo}\n")
            f.write(f"Content:\n{contenido_archivo}\n")
            f.write('-' * 40 + '\n')
        
        print(f'Commit realizado: "{mensaje_commit}"')
    else:
        print("Error: El archivo o el repositorio no existen.")
