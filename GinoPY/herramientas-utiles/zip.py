# Ejemplo de la función zip() en Python
# zip() combina elementos de varios iterables en tuplas

# Preparamos dos listas con la misma cantidad de elementos
nombres = ["Ana", "Juan", "Pedro"]
edades = [25, 30, 35]

# Usamos zip() para emparejar cada nombre con su edad correspondiente
# zip(nombres, edades) crea un iterador de tuplas: ("Ana", 25), ("Juan", 30), etc.
personas = zip(nombres, edades)

# Mostramos el resultado recorriéndolo con un bucle for
print("Personas y sus edades:")
# 'nombre' toma el primer elemento de la tupla y 'edad' el segundo
for nombre, edad in personas:
    print(f"{nombre} tiene {edad} años")

# También podemos convertir el zip en una lista de tuplas directamente
print("\nLista de tuplas creada con zip:")
nombres_y_edades = list(zip(nombres, edades))
print(nombres_y_edades)
