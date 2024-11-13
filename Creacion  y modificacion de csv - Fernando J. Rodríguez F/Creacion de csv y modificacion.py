import csv

# 1. Crear el archivo .csv con una lista de alumnos
alumnos = [
    {"Nombre": "Juan Perez", "Edad": 20, "Calificacion": 85},
    {"Nombre": "Ana Gomez", "Edad": 22, "Calificacion": 90},
    {"Nombre": "Luis Rodriguez", "Edad": 21, "Calificacion": 88}
]

with open("lista_alumnos.csv", mode="w", newline="") as archivo:
    campos = ["Nombre", "Edad", "Calificacion"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()  # Escribe los nombres de las columnas
    escritor.writerows(alumnos)  # Escribe los datos de los alumnos

print("Archivo 'lista_alumnos.csv' creado con exito.")

# 2. Modificar el archivo .csv para anadir un nuevo alumno
nuevo_alumno = {"Nombre": "Carla Torres", "Edad": 23, "Calificacion": 92}

with open("lista_alumnos.csv", mode="a", newline="") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writerow(nuevo_alumno)  # Anade el nuevo alumno

print("Nuevo alumno anadido al archivo 'lista_alumnos.csv'.")

# 3. Leer el archivo .csv para verificar los datos
with open("lista_alumnos.csv", mode="r", newline="") as archivo:
    lector = csv.DictReader(archivo)
    print("Contenido del archivo 'lista_alumnos.csv':")
    for fila in lector:
        print(fila)
