from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola mundo"}

@app.get("/usuario/{nombre}")
def leer_usuario(nombre: str):
    return {"usuario": nombre}
