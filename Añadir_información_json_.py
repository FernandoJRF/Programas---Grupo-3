#Se importaq la biblioteca json para trabajar con archivos json
import json
#Se define la ruta del archivo Json
file_path = 'informations.json'
#Se crea un diccionario con la nueva información que se desea añadir
new_information = {
     "name":"Ana",
    "last_name": "Martinez",
    "age": "72",
    "email":"Anama03@gmail.com",
    "PasaTiempos": [
        "Cocina Gourmet",
        "Lectura de Novelas",
    ],
    "address": {
        "street": "Calle 50",
        "city": "Panama City",
        "codigo_postal": "0830"
    }
   
} 
# Se abre el archivo en modo lectura('r') para cargar la información actual
with open (file_path, mode ='r') as file:
#Se lee el contenido actual del archivo y se guarda en una lista de diccionarios

     informations = json.load(file)
# Se agrega la nueva información al final de la lista de diccionarios
informations.append(new_information)
#Se abre el archivo en modo de escritura('w') para actualizar el contenido con la información añadida
with open (file_path, mode= 'w') as file:
    json.dump(informations, file, indent=4)
#Se actualiza la lista de diccionarios en el archivo Json con una identación de 4 espacios
