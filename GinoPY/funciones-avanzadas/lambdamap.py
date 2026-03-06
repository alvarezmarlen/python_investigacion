# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usamos map() para aplicar una operación a cada número de la lista
# lambda x: x**2
# x -> cada número de la lista
# **2 -> elevar el número al cuadrado

cuadrados = list(map(lambda x: x**2, numeros))

# list() convierte el resultado de map en una lista normal

# Mostramos el resultado
print("Números al cuadrado:", cuadrados)