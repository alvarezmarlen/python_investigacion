# Importamos Flask y la función render_template para poder renderizar archivos HTML
from flask import Flask, render_template

# Creamos una instancia de la aplicación Flask
app2 = Flask(__name__)

# Definimos la ruta principal de la aplicación ("/")
@app2.route("/")
def inicio():
    # Renderiza el archivo index.html cuando se accede a la ruta "/"
    return render_template("index.html")

# Definimos una ruta que recibe un parámetro <nombre>
@app2.route("/saludo/<nombre>")
def saludo(nombre):
    # Renderiza el archivo saludo.html y le pasa la variable 'nombre'
    return render_template("saludo.html", nombre=nombre)

# Este bloque asegura que la aplicación se ejecute solo si el script es ejecutado directamente
if __name__ == "__main__":
    # Ejecuta la aplicación en modo debug, útil para desarrollo
    app2.run(debug=True)