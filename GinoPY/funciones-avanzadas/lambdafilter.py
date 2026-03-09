# Lista de edades
edades = [12, 17, 18, 21, 15, 30]

# Usamos filter() para quedarnos solo con las edades mayores o iguales a 18
# lambda edad: edad >= 18
# edad -> cada número de la lista
# >= 18 -> condición para saber si es mayor de edad

mayores = list(filter(lambda edad: edad >= 18, edades))

# list() convierte el resultado de filter en una lista normal

# Mostramos el resultado
print("Personas mayores de edad:", mayores)