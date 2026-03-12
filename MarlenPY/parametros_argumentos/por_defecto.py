# El Argumento es Opcional porque el Parámetro ya tiene un valor por Defecto en 'part2'
def nombre_curso(part1, part2, part3="Bolueta"):
    print(f"{part1} {part2} {part3}")
    
nombre_curso("Peñascal", "F5")    # Si el 3er argumento no se envía => Python usa el valor por defecto ("Bolueta").

nombre_curso("Peñascal", "F5", "FullStack")   # Sí la llamada tiene datos => Manda el Argumento que coloquemos.

