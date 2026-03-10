# Nombre es una variable global
# Accesible desde la función
# mostrar_nombre() imprime Carlos

nombre = "Carlos"  # variable global

def mostrar_nombre():
    print(nombre)

mostrar_nombre()  # imprime: Carlos