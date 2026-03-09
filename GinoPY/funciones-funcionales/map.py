# Ejemplo de la función map en Python (sin usar lambda)
# map() aplica una función a cada elemento de un iterable

# Definimos una función convencional que convierte un número a su cuadrado
def calcular_cuadrado(n):
    return n ** 2

# Lista de números de ejemplo
numeros = [1, 2, 3, 4, 5]

# Usamos map para aplicar la función 'calcular_cuadrado' a cada elemento de la lista
# map(función, iterable)
# En este caso pasamos el nombre de la función definida arriba y la lista
resultado_map = map(calcular_cuadrado, numeros)

# Convertimos el objeto map en una lista para poder imprimirlo
cuadrados = list(resultado_map)

# Mostramos los resultados
print("Lista original:", numeros)
print("Cuadrados calculados con map:", cuadrados)
