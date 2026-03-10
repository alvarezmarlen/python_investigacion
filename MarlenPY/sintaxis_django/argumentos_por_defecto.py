# El parámetro 'part2' tiene un valor por defecto
def nombre_curso(part1, part2="F5"):
    print(f"{part1} {part2}")
    
nombre_curso("Peñascal") 



# Caso B: Sí envía el argumento (Sobrescribe)
nombre_curso("Peñascal", "Python") 

""" "El Argumento es Opcional porque el Parámetro ya tiene un valor por Defecto."
Si la llamada está vacía     Manda el Parámetro ("F5").
Si la llamada tiene datos    Manda el Argumento ("Python"). """