import os

def init_repo(nombre_repo):
    # Crear una carpeta con el nombre del repositorio
    if not os.path.exists(nombre_repo):
        os.mkdir(nombre_repo)
        print(f'Repositorio "{nombre_repo}" creado.')
        
        # Crear la carpeta ".git" dentro del repositorio
        directorio_git = os.path.join(nombre_repo, ".git")
        os.mkdir(directorio_git)
        print(f'Carpeta ".git" creada dentro de {nombre_repo}.')
    else:
        print(f'El repositorio "{nombre_repo}" ya existe.')

def make_commit(nombre_repo, nombre_archivo):
    # Comprobar que el repositorio y el archivo existen
    directorio_git = os.path.join(nombre_repo, ".git")
    
    if os.path.exists(directorio_git) and os.path.exists(os.path.join(nombre_repo, nombre_archivo)):
        # Leer el contenido del archivo
        with open(os.path.join(nombre_repo, nombre_archivo), 'r') as f:
            contenido_archivo = f.read()
        
        # Mostrar el contenido leído
        print(f"Contenido del archivo '{nombre_archivo}':\n{contenido_archivo}")
    else:
        print("Error: El archivo o el repositorio no existen.")

# Probamos la función
nombre_repo = "mi_repositorio"
nombre_archivo = "prueba.txt"
init_repo(nombre_repo)
make_commit(nombre_repo, nombre_archivo)
