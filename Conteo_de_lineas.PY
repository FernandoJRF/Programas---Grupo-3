
# Conteo de las líneas del texto con entrada de usuario y registrando los resultados

# Abrir el archivo de registro donde se almacenarán los resultados
with open('registro_conteo_lineas.txt', 'a') as registro_file:
    while True:
        # Solicitar al usuario que ingrese el nombre del archivo
        archivo = input("Por favor, ingresa el nombre del archivo (con su extensión) o escribe 'salir' para terminar: ")

        # Si el usuario escribe 'salir', se termina el ciclo
        if archivo.lower() == 'salir':
            print("\n✨ ¡Hasta luego! Gracias por usar el programa. ✨")
            break

        # Abrir el archivo y contar las líneas
        try:
            with open(archivo, 'r') as file:
                lines = file.readlines()
                line_count = len(lines)
            
                # Mostrar el resultado 
                print(f"\n✨ Conteo de líneas en el archivo '{archivo}' ✨")
                print(f"Total de líneas encontradas: {line_count}\n")

                # Registrar el resultado en el archivo de registro
                registro_file.write(f"Archivo: {archivo} - Total de lineas: {line_count}\n")
        except FileNotFoundError:
            print(f" ⚠️  El archivo '{archivo}' no se encuentra en la ubicacion especificada.\n")
            registro_file.write(f"Archivo: {archivo} - Error: No se encontro el archivo\n")
        except Exception as e:
            print(f"🔴 Ocurrió un error: {e}\n")
            registro_file.write(f"Archivo: {archivo} - Error: {e}\n")

