import random
import secrets
import string
from cryptography.fernet import Fernet

def genera_contra(lon):
    if (lon < 8 or lon > 16):
        return "Longitud no apta" #this could be do it in a validation method
    else: 
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña = ''
        for i in range(0,lon):
            contraseña += secrets.choice(caracteres)
        return contraseña

def master_key():
    key = Fernet.generate_key()
    with open('clave.key','wb') as clave:
        clave.write(key)

def load_key():
    return open('clave.key','rb').read()

def cifrar_cadena(key,cadena):
    f = Fernet(key)
    return f.encrypt(cadena.encode())

def descifrar_cadena(key,cadena):
    f = Fernet(key)
    return f.decrypt(cadena).decode() 

