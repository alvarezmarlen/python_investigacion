""" El Argumento es Opcional porque el Parámetro ya tiene un valor por Defecto. """
# El parámetro 'part2' tiene un valor por defecto
def nombre_curso(part1, part2="F5"):
    print(f"{part1} {part2}")
    
nombre_curso("Peñascal")    # Si la llamada está vacía  =>  Manda el Parámetro ("F5").


# Sí la llamada tiene datos => Manda el Argumento ("Python").
nombre_curso("Peñascal", "Python") 

