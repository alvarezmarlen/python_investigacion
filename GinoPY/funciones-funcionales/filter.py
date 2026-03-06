# Creamos una lista de números
numeros = [1, 2, 3, 4, 5, 6]

# Usamos filter() para filtrar elementos de la lista
# lambda x: x % 2 == 0 es una función pequeña que:
# - recibe un número (x)
# - comprueba si el número es par
# % es el operador módulo (resto de la división)

pares = list(filter(lambda x: x % 2 == 0, numeros))

# list() convierte el resultado de filter en una lista normal

# Imprimimos el resultado en pantalla
print("Números pares:", pares)