import os

def init_repo(nombre_repo):
    # Crear una carpeta con el nombre del repositorio
    if not os.path.exists(nombre_repo):
        os.mkdir(nombre_repo)
        print(f'Repositorio "{nombre_repo}" creado.')
        
        # Crear la carpeta ".git" dentro del repositorio
        git_dir = os.path.join(nombre_repo, ".git")
        os.mkdir(git_dir)
        print(f'Carpeta ".git" creada dentro de {nombre_repo}.')
    else:
        print(f'El repositorio "{nombre_repo}" ya existe.')

# Probamos la función
nombre_repo = "mi_repositorio"
init_repo(nombre_repo)
