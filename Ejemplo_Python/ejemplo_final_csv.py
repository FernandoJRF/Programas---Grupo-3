import csv
from calendar import monthrange
# Leer un archivo CSV
with open('meses.csv', mode='r') as file:
    csv_reader = csv.DictReader(file) 
    for row in csv_reader:             
        print(row)
# Mostrar la información por columnas
with open('meses.csv', mode='r') as file:
    csv_reader = csv.DictReader(file) 
    for row in csv_reader:
        print(f"Num: {row['num']}, Mes: {row['mes']}, Estacion: {row['estacion']}")
        
new_product = {
    'num': '12',
    'mes': 'Diciembre',
    'estacion': 'Invierno'
}

# Añadir un nuevo producto (fila) al archivo CSV en modo 'append'
new_product = {
    'num': '12',
    'mes': 'Diciembre',
    'estacion': 'Invierno'
}
file_path = 'meses.csv'
updated_file_path = 'meses_updated.csv'
def obtener_dias_del_mes(mes, año=2024):
    # monthrange devuelve un par (primer_día, número_de_días)
    return monthrange(año, int(mes))[1]
with open(file_path, mode='a', newline='') as file:
    # Definir un DictWriter con las claves de new_product
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    
    # Escribir la nueva fila
    csv_writer.writerow(new_product)

# Crear un archivo actualizado con una columna adicional para los días del mes
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Obtener los nombres de las columnas existentes y añadir 'total_value'
    fieldnames = csv_reader.fieldnames + ['total_value']
    
    # Archivo actualizado
    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        
        #  Los encabezados
        csv_writer.writeheader()
        
        for row in csv_reader:
            # Asumimos que 'num' es la columna que contiene el número del mes (1 a 12)
            mes = int(row['num'])
            # Calcular el total de días 
            row['total_value'] = obtener_dias_del_mes(mes, año=2024)
            csv_writer.writerow(row)
