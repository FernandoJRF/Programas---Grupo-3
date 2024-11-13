import json

# Especifica la ruta de tu archivo JSON
archivo_json = 'product_limpieza.json'

# Lee el archivo JSON
with open(archivo_json, 'r') as archivo:
    contenido = json.load(archivo)

# Muestra el contenido del archivo
print("Listado de productos de limpieza:")
for producto in contenido["productos"]:
    print(f"Nombre: {producto['nombre']}")
    print(f"Descripción: {producto['descripcion']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Disponible: {'Sí' if producto['disponible'] else 'No'}")
    print("-" * 30)
