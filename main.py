import secrets
import string

def generar_password(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return password

print("Tu contraseña segura es:")
print(generar_password())