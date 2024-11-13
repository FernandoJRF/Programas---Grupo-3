
#Leer un archivo lí­nea por lí­nea
# lectura (‘r’): Este modo abre los archivos de texto solo para lectura.
with open('Bosque_encantado.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())