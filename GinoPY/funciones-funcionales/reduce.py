# Ejemplo de la función reduce en Python (sin usar lambda)
# reduce() aplica una función de forma acumulativa a los elementos de una lista

# Importamos reduce desde el módulo functools (necesario en Python 3)
from functools import reduce

# Definimos una función convencional que suma dos números
def sumar_elementos(a, b):
    # 'a' es el valor acumulado y 'b' es el siguiente elemento de la lista
    return a + b

# Lista de números de ejemplo
numeros = [1, 10, 20, 30]

# Usamos reduce para obtener la suma total de todos los elementos
# reduce(función, iterable)
suma_total = reduce(sumar_elementos, numeros)

# Imprimimos el resultado final
print("Lista de entrada:", numeros)
print("Resultado final de la suma con reduce:", suma_total)
