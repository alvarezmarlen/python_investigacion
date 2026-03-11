# función flexible que crea un perfil de usuario dinámico usando argumentos 
# posicionales (*args) y argumentos con nombre (**kwargs).

def crear_perfil_dinamico(usuario_id, *args, **kwargs):
    
    # Lista de claves que se usarán para asignar los argumentos posicionales
    claves_args = ["nombre", "apellido", "segundo_apellido"]
    
     # Creamos el diccionario base del perfil con el ID del usuario
    perfil = {"id": usuario_id}
    
    # Recorremos los argumentos posicionales (*args)
    # enumerate() devuelve pares (indice, valor)
    # ejemplo: (0, "Ana")
    for i, valor in enumerate(args):

         # Si todavía hay claves definidas en claves_args
        if i < len(claves_args):
             # Asignamos el valor a la clave correspondiente
            perfil[claves_args[i]] = valor
        else:
            # Si hay más argumentos que claves disponibles,
            # los guardamos como campos extra dinámicos extra_1, extra_2, etc.
            perfil[f"extra_{i - len(claves_args) + 1}"] = valor
    
    # Añadimos al diccionario todos los argumentos con nombre (**kwargs)
    # update() inserta cada par clave-valor dentro del diccionario
    perfil.update(kwargs)
    
    # Devolvemos el diccionario final con toda la información del usuario
    return perfil

# Ejemplo de uso
perfil1 = crear_perfil_dinamico(
    101,
    "Ana", "García",       
    edad=28,
    ciudad="Madrid",
    ocupacion="Ingeniera"
)

perfil2 = crear_perfil_dinamico(
    102,
    "Luis", "Pérez", "Santos",
    ciudad="Barcelona",
    hobby="Futbol"
)

perfil3 = crear_perfil_dinamico(
    103,
    "Marta",                 
    "Lopez",                    
    "ExtraDato1", "ExtraDato2",  
    profesion="Doctora"
)

print(perfil1)
print(perfil2)
print(perfil3)