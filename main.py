import random
import secrets
import string

def genera_contra(lon):
    if (lon < 8 or lon > 16):
        return "Longitud no apta" #this could be do it in a validation method
    else: 
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña = ''
        for i in range(0,lon):
            contraseña += secrets.choice(caracteres)
        return contraseña

print(genera_contra(8))