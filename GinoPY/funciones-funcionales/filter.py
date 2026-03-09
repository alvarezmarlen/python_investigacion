# Ejemplo de la función filter en Python (sin usar lambda)
# filter() crea un iterador con los elementos que cumplen una condición determinada

# Definimos una función que devuelve True si el número es par
def comprobar_si_es_par(n):
    # Si el resto de dividir entre 2 es 0, es par
    return n % 2 == 0

# Lista de números de ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usamos filter para quedarnos solo con los números que pasan la prueba de la función
# filter(función, iterable)
# Pasamos la función 'comprobar_si_es_par' sin paréntesis y la lista de números
resultado_filter = filter(comprobar_si_es_par, numeros)

# Convertimos el resultado en una lista para mostrarlo
pares = list(resultado_filter)

# Imprimimos los resultados en consola
print("Lista original:", numeros)
print("Números filtrados (solo pares):", pares)