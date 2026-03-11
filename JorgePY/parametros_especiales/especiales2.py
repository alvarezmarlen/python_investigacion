# función flexible para crear perfiles de usuario 
# usando argumentos posicionales variables

def crear_perfil(usuario_id, *args, **kwargs):
    # Aqui se crea un diccionario
    # id el valor de usuario_id
    # todos los valores recibidos en *args
    
    perfil = {
        "id": usuario_id,
        "nombres_extra": args,
    }
    # Agregamos todos los datos con nombre
    # kwargs es un diccionario con los argumentos nombrados.
    # El for recorre cada par y los agrega al diccionario perfil.
    for clave, valor in kwargs.items():
        perfil[clave] = valor
    return perfil

# Ejemplo de uso
perfil1 = crear_perfil(
    101,
    "Ana", "García",
    edad=28,
    ciudad="Madrid",
    ocupacion="Ingeniera"
)

perfil2 = crear_perfil(
    102,
    "Luis",
    edad=35,
    ciudad="Barcelona"
)

print(perfil1)
print(perfil2)