import secrets
import string
import os
import json
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

def guardar_creedenciales(servicio, usuario, contraseña, file = "password.json"):
    clave = load_key()

    creedenciales_a_guardar = {
        "usuario": cifrar_cadena(clave, usuario),
        "contraseña": cifrar_cadena(clave, contraseña)
    }

    if os.path.exists(file):
        with open(file,'r') as archivo_salida:
            data = json.load(archivo_salida)
    else:
        data = {}

    data[servicio] = creedenciales_a_guardar

    with open(file,'wb') as archivo_a_guardar:
        json.dump(data, archivo_a_guardar)
    
    print(f"Creedenciales para {servicio} guardadas correctamente")

def leer_credenciales(servicio, file='password.json'):
    clave = load_key()
    if os.path.exists(file):
        with open(file,'rb') as archivo_entrada:
            data = json.load(archivo_entrada)
        if servicio in data:
            usuario = descifrar_cadena(clave, data[servicio]["usuario"])
            contraseña = descifrar_cadena(clave, data[servicio]["contraseña"])
            print(f"Servicio: {servicio} \nUsuario: {usuario} \nContraseña: {contraseña}")
        else:
            print(f"No se encontraron credenciales para {servicio}")
    else:
        print("No se encontraron credenciales")
    