# Ejemplo de función lambda con map en Python
# map() aplica una función a todos los elementos de una lista

# Definimos una lista de números
numeros = [1, 2, 3, 4, 5]

# Usamos lambda para definir la función que eleva cada número al cuadrado
# map(función, iterable) recibe:
# 1. lambda x: x ** 2 -> función anónima que toma x y devuelve su cuadrado
# 2. numeros -> la lista sobre la que queremos iterar
cuadrados = list(map(lambda x: x ** 2, numeros))

# Imprimimos el resultado
# list() se usa para convertir el objeto map en una lista legible
print("Lista original:", numeros)
print("Números al cuadrado con lambda y map:", cuadrados)