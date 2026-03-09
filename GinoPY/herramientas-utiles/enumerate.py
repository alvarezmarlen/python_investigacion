# Ejemplo de la función enumerate() en Python
# enumerate() añade un contador a un iterable y lo devuelve en forma de objeto enumerado

# Definimos una lista de frutas
frutas = ["manzana", "platano", "cereza", "pera"]

# Usamos enumerate() en un bucle for
# enumerate(frutas) devuelve pares de (índice, valor)
# 'i' será el índice (empieza en 0 por defecto)
# 'fruta' será el elemento de la lista
for i, fruta in enumerate(frutas):
    # Imprimimos el índice y el nombre de la fruta
    print(f"Índice {i}: {fruta}")

# Ejemplo avanzado: empezar el contador en 1 en lugar de 0
print("\nLista con el contador empezando en 1:")
for i, fruta in enumerate(frutas, start=1):
    print(f"Producto {i}: {fruta}")
