#Este programa genera contraseña
import random
import string

def generate_password(length):
    # selecionamos los caracteres que queremos que tenga nuestra contraseña
    characters = string.ascii_letters + string.digits + string.punctuation
    # genera una contraseña aleatoria con la longitud
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#pedir la contraseña que desee el usuario
password_length = int(input("Introduce la longitud de la contraseña: "))

# generar y dar la contraseña
password = generate_password(password_length)
print(f"Tu contraseña generada es: {password}")
