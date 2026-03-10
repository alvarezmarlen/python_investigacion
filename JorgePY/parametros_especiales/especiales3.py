def crear_perfil_dinamico(usuario_id, *args, **kwargs):
    # Claves predefinidas para los args posicionales
    claves_args = ["nombre", "apellido", "segundo_apellido"]
    
    perfil = {"id": usuario_id}
    
    # Asignamos los args a las claves correspondientes
    # enumerate toma una coleccion y devuelve un enumerado
    for i, valor in enumerate(args):
        if i < len(claves_args):
            perfil[claves_args[i]] = valor
        else:
            # Si hay más args que claves, los guardamos como adicionales
            perfil[f"extra_{i - len(claves_args) + 1}"] = valor
    
    # Agregamos los kwargs al perfil
    # update inserta items en un diccionario
    perfil.update(kwargs)
    
    return perfil

# Ejemplo de uso
perfil1 = crear_perfil_dinamico(
    101,
    "Ana", "García",          # nombre y apellido
    edad=28,
    ciudad="Madrid",
    ocupacion="Ingeniera"
)

perfil2 = crear_perfil_dinamico(
    102,
    "Luis", "Pérez", "Santos", # nombre, apellido y segundo apellido
    ciudad="Barcelona",
    hobby="Futbol"
)

perfil3 = crear_perfil_dinamico(
    103,
    "Marta",                    # solo nombre
    "Lopez",                     # apellido
    "ExtraDato1", "ExtraDato2",  # datos extra sin clave predefinida
    profesion="Doctora"
)

print(perfil1)
print(perfil2)
print(perfil3)