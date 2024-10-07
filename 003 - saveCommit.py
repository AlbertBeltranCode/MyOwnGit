import os
import time

#Declaramos una funcion inicial donde se crearan las carpetas y los ficheros necesarios
def init_repo(nombre_repo):
    # Creamos una carpeta con el nombre del repositorio
    if not os.path.exists(nombre_repo):
        os.mkdir(nombre_repo)
        print(f'Repositorio "{nombre_repo}" creado.')
        
        # Creamos la carpeta ".git" dentro del repositorio
        directorio_git = os.path.join(nombre_repo, ".git")
        os.mkdir(directorio_git)
        print(f'Carpeta ".git" creada dentro de {nombre_repo}.')
        
        # Creamos el archivo commits.txt dentro de la carpeta .git
        archivo_commit = os.path.join(directorio_git, 'commits.txt')
        with open(archivo_commit, 'w') as f:
            f.write('')  # Creamos el archivo vacío
        print(f'Archivo "commits.txt" creado dentro de {directorio_git}.')
    else:
        print(f'El repositorio "{nombre_repo}" ya existe.')

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
        
        # Depuramos para asegurarnos de que esta funcionando correctamente
        print(f'Intentando escribir en: {archivo_commit}')
        print(f'Contenido del archivo {nombre_archivo} que se va a commitear:\n{contenido_archivo}')
        
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

# Asignamos valores a las funciones
nombre_repo = "mi_repositorio"
nombre_archivo = "archivo.txt"  # Archivo del que hacemos commit

# Inicializamos el repositorio y creamos asi las carpetas y el fichero commits.txt automáticamente
init_repo(nombre_repo)

# Creamos un archivo al cual vamos a hacer commit
with open(os.path.join(nombre_repo, nombre_archivo), 'w') as f:
    f.write("Este es el contenido del archivo que voy a commitear.")

# Realizamos un commit
hacer_commit(nombre_repo, nombre_archivo, "Mi primer commit")
