import os

#Declaramos una funcion inicial donde se crearan las carpetas y los ficheros necesarios
def init_repo(nombre_repo):
    # Crear una carpeta con el nombre del repositorio
    if not os.path.exists(nombre_repo):
        os.mkdir(nombre_repo)
        print(f'Repositorio "{nombre_repo}" creado.')
        
        # Crear la carpeta ".git" dentro del repositorio
        directorio_git = os.path.join(nombre_repo, ".git")
        os.mkdir(directorio_git)
        print(f'Carpeta ".git" creada dentro de {nombre_repo}.')
        
        # Crear el archivo commits.txt dentro de la carpeta .git
        archivo_commit = os.path.join(directorio_git, 'commits.txt')
        with open(archivo_commit, 'w') as f:
            f.write('')  # Crear el archivo vacío
        print(f'Archivo "commits.txt" creado dentro de {directorio_git}.')
        
         # Crear la carpeta staging dentro de .git
        staging_dir = os.path.join(directorio_git, 'staging')
        os.mkdir(staging_dir)  # Asegúrate de usar os.mkdir para crear un directorio
        print(f'Carpeta "staging" creada dentro de {directorio_git}.')
    else:
        print(f'El repositorio "{nombre_repo}" ya existe.')
