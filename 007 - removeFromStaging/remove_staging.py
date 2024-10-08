import os

# funcion para eliminar un archivo dentro de la carpeta staging
def remover_de_staging(nombre_repo, nombre_archivo):
    directorio_git = os.path.join(nombre_repo, ".git")
    staging_dir = os.path.join(directorio_git, 'staging')
    archivo_staging = os.path.join(staging_dir, nombre_archivo)
    
    # Verificar si el archivo existe en el área de staging
    if os.path.exists(archivo_staging):
        os.remove(archivo_staging)  # Eliminar el archivo de la carpeta staging
        print(f'Archivo "{nombre_archivo}" removido del área de staging.')
    else:
        print(f'Error: El archivo "{nombre_archivo}" no está en el área de staging.')
