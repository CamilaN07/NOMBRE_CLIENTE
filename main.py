from fastapi import FastAPI
from datetime import datetime

mi_app = FastAPI()

@mi_app.get("/")
def inicio():
    return {"mensaje": "Hola aprendices 3407180"}

@mi_app.get("/saludar")
def saludar():
    return {"saludo": "Hola soy ... "}

"""IMPORTAR datetime
mostrar la hora actual del servidor
"""
#AHORA

@mi_app.get("/hora")
def dar_hora():
    return {"Hora": datetime.now()}
        
#
@mi_app.get("/saludar/{nombre}")
def saludar2(nombre, apellido, edad):
    return {"saludo": f"Hola soy {nombre} {apellido} {edad}"}
"""
1.Crear otro enpoint uno en el que me retorne una lista (min 5)
de amigos.

2.Crear otro enpoint en el que me retorne un solo amigo"""

#LISTA
@mi_app.get("/amigos")
def lista_amigos():
    amigos = [
        "Camila",
        "Maria",
        "Luis",
        "Sofía",
        "Diego",
        "Juan",
    ]
    return {"amigos":amigos}

# {id} será la posición en la lista (0 para Carlos, 1 para Ana, etc.)

@mi_app.get("/amigos/{id}")
def amigo(id: int):
    lista_amigos = [
        "Camila",
        "Maria",
        "Luis",
        "Sofía",
        "Diego",
        "Juan",
    ]
    
    #ID debe existir en la lista (0 a 5)
    if id < 0 or id >= len(lista_amigos):
        return {"error": "No esta"}
        
    return {"amigo": lista_amigos[id]}