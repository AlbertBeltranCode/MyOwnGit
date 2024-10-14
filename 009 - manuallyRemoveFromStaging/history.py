import os

#Declaramos una funcion para mostrar_historial el historial de commits.
def mostrar_historial(nombre_repo):
    directorio_git = os.path.join(nombre_repo, ".git")
    archivo_commit = os.path.join(directorio_git, 'commits.txt')
    
    # Comprobar que el archivo de commits existe
    if os.path.exists(archivo_commit):
        with open(archivo_commit, 'r') as f:
            historial = f.readlines()
        
        print("Historial de Commits:")
        for linea in historial:
            print(linea.strip())  # Imprimir cada línea sin saltos de línea extra
    else:
        print("Error: No se encontró el archivo de commits.")
