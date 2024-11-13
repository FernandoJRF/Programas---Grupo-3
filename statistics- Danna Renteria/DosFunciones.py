#Uso de dos funciones
#Area de un cilindro
def area_cilindro(r,h):
    import math
    area=2*(math.pi)*r*h+2*(math.pi)*(r**2)
    redo=round(area,2)
    return redo
#Volumen de un cilindro
def volumen_cilindro(r,h):
    import math
    volumen=(math.pi)*(r**2)*h
    redo=round(volumen,2)
    return redo
#Cuerpo principal
while True:
    print()
    print("Bienvenid@")
    try:
        radio=float(input("Introduzca el valor del radio: "))
        altura=float(input("Introduzca el valor de la altura: "))
#Menú
        print("""
            Menú Principal:
            1. Area de un cilindro 
            2. Volumen de un cilindro
            0. Salir
            """)
        opcion=int(input("Escoge una opción: "))
        if opcion==1:
            resultado=area_cilindro(radio,altura)
            print("El area del cilindro es de =", resultado) 
        elif opcion==2:
            resultado=volumen_cilindro(radio, altura)
            print("El volumen del cilindro es de =", resultado)
        elif opcion==0:
            print("Fin del programa")
            break
        else:
            print("Ups. Escoge una de las opciones del menú")
    except:
        print("Debe ingresar un valor numerico o diferente de 0")