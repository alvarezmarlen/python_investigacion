def crear_perfil(usuario_id, *args, **kwargs):
    perfil = {
        "id": usuario_id,
        "nombres_extra": args,  # cualquier dato adicional posicional
    }
    # Agregamos todos los datos con nombre
    for clave, valor in kwargs.items():
        perfil[clave] = valor
    return perfil

# Ejemplo de uso
perfil1 = crear_perfil(
    101,
    "Ana", "García",       # args: nombres adicionales
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