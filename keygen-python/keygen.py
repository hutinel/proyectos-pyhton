import secrets
import string

caracteres = string.ascii_letters + string.digits + string.punctuation
longitud = 12
contraseña = ''.join(secrets.choice(caracteres) for i in range(longitud))

print(f"Tu nueva contraseña es: {contraseña}")

#Asegura que la contraseña tenga al menos una letra, un número y un símbolo
while True:
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    if (any(c.islower() for c in contraseña) and
        any(c.isupper() for c in contraseña) and
        any(c.isdigit() for c in contraseña) and
        any(c in string.punctuation for c in contraseña)):
        break

print(f"Tu nueva contraseña segura es: {contraseña}")

#Permite generar múltiples contraseñas
for _ in range(5):
    print(''.join(secrets.choice(caracteres) for _ in range(longitud)))    

print(f"Tu nueva contraseña segura es: {contraseña}")