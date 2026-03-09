# Importamos Flask desde la librería flask
from flask import Flask

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Definimos la ruta principal "/" de la aplicación
@app.route("/")
def inicio():
    # Retorna un mensaje de saludo cuando se accede a la ruta "/"
    return "Hola, esta es mi primera app con Flask"

# Definimos una ruta que acepta un parámetro <nombre>
@app.route("/saludo/<nombre>")
def saludo(nombre):
    # Retorna un mensaje personalizado usando el nombre recibido en la URL
    return f"Hola {nombre}, bienvenido a Flask!"

# Este bloque asegura que la aplicación se ejecute solo si el script se ejecuta directamente
if __name__ == "__main__":
    # Ejecuta la aplicación en modo debug para facilitar el desarrollo
    app.run(debug=True)