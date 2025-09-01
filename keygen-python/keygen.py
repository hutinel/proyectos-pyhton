import secrets
import string

caracteres = string.ascii_letters + string.digits + string.punctuation
longitud = 16
contraseña = ''.join(secrets.choice(caracteres) for i in range(longitud))

print(f"Tu nueva contraseña es: {contraseña}")