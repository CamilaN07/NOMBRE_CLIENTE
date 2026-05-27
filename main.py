from fastapi import FastAPI

app = FastAPI()

# Endpoint principal "/"
@app.get("/")
def inicio():
    return {"mensaje": "Este es el proyecto de clientes a desarrollar"}

# Endpoint "/clientes"
@app.get("/clientes")
def obtener_clientes():
    clientes = [
        "Camila",
        "Sebastian",
        "Matías",
        "Carmenza"
    ]
    
    return {"clientes": clientes}
