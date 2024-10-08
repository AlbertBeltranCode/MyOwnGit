import os
import shutil

#Creamos una funcion para copiar el archivo al cual hacemos commit dentro de la carpeta staging
def agregar_a_staging(nombre_repo, nombre_archivo):
    directorio_git = os.path.join(nombre_repo, ".git")
    staging_dir = os.path.join(directorio_git, 'staging')
    
    if os.path.exists(os.path.join(nombre_repo, nombre_archivo)):
        # Copiar el archivo al área de staging
        shutil.copy(os.path.join(nombre_repo, nombre_archivo), staging_dir)
        print(f'Archivo "{nombre_archivo}" agregado a la carpeta "staging".')
    else:
        print(f'Error: El archivo "{nombre_archivo}" no existe en el repositorio.')
