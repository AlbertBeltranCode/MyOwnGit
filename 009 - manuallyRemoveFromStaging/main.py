from init_repo import init_repo
from commit import hacer_commit
from history import mostrar_historial
from staging import agregar_a_staging
from remove_staging import remover_de_staging
import os

# Asignamos valores a las funciones
nombre_repo = "mi_repositorio"
nombre_archivo = "archivo.txt" # Archivo del que hacemos commit

# Inicializamos el repositorio
init_repo(nombre_repo)

# Creamos un archivo para hacer commit
with open(os.path.join(nombre_repo, nombre_archivo), 'w') as f:
    f.write("Este es el contenido del archivo que voy a commitear.")

# Agregamos el archivo al área de staging
agregar_a_staging(nombre_repo, nombre_archivo)

# Decidimos remover el archivo del área de staging antes del commit para comprobar que se elimina correctamente
remover_de_staging(nombre_repo, nombre_archivo)

# Realizamos un commit 
hacer_commit(nombre_repo, nombre_archivo, "Mi primer commit")

# Mostramos el historial de commits
mostrar_historial(nombre_repo)
