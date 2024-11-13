import os

print("\nCrear un archivo")
print("================")

NOMBRE_ARCHIVO = 'datos.txt'

# Crear y abrir el archivo en modo escritura
with open(NOMBRE_ARCHIVO, 'w') as archivo:
    archivo.write('Este es una prueba \ny otra prueba.')

# Verificar si el archivo fue creado
if NOMBRE_ARCHIVO in os.listdir("."):
    print("\nArchivo creado en la ruta: \n\n\t{0}/{1}".format(os.getcwd(), NOMBRE_ARCHIVO))
else:
    print("El archivo no fue creado!!!\n")

print("\n\nLeer un archivo")
print("===============\n")

# Leer el contenido del archivo
with open(NOMBRE_ARCHIVO, 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

print("\n\nIterar sobre un archivo")
print("=======================\n")

# Iterar sobre las líneas del archivo
with open(NOMBRE_ARCHIVO, 'r') as archivo:
    for linea in archivo:
        print(linea, end='')  # end='' evita agregar una nueva línea extra

print("\n")
    
print("\nEliminar un archivo")
print("===================")

# Eliminar el archivo
os.remove(os.path.join(os.getcwd(), NOMBRE_ARCHIVO))
print("\nEliminado archivo desde la ruta: \n\n\t{0}/{1}".format(os.getcwd(), NOMBRE_ARCHIVO))