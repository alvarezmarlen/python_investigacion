# Mensaje es una variable local en la función saludar
# No accesible fuera de la función
# saludar() imprime "Hola Mundo"
# print(mensaje) produce error

def saludar():
    mensaje = "Hola Mundo"  # variable local
    print(mensaje)

saludar()
print(mensaje)