# 3. Definimos la función que devuelve una Colección (una Lista [])
def obtener_sedes():
    lista_sedes = ["Peñascal", "Bolueta", "Madrid"]    # Creamos una lista con varios elementos
    return lista_sedes

mis_sedes = obtener_sedes()     # 2. "Atrapamos" la lista completa en una variable
print(mis_sedes)                # 3. Ahora podemos usar esa variable para lo que queramos

# 4. Ejemplo de REUTILIZACIÓN:
# Como es una lista, podemos saber cuántas sedes hay
print(f"En total tenemos {len(mis_sedes)} sedes.")