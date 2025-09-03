import datetime
import secrets
import string


ahora = datetime.datetime.now()
mes = ahora.strftime("%b")
dia_numero = ahora.strftime("%d")
ano_numero = ahora.strftime("%Y")
hora = ahora.strftime("%H%M%S")
letra_aleatoria = string.ascii_letters.lower()
parte_aleatoria = ''.join(secrets.choice(letra_aleatoria) for _ in range(1))

contraseña_patron = f"#{mes.upper()}{dia_numero}{ano_numero}{parte_aleatoria}{hora}.#"

print(f"su nueva contraseña es: {contraseña_patron}")


