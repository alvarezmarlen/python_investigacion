# --- INVESTIGACIÓN: PASO POR REFERENCIA (Objetos Mutables) ---
mi_lista = [1, 2, 3]  # ARGUMENTO: El objeto original en memoria.

def modificar_lista(lista_recibida): # PARÁMETRO (Recibe la referencia)
    lista_recibida.append(4)         # Actúa sobre la lista original.

modificar_lista(mi_lista) # INVOCACIÓN: Le entregamos el "mando" a la función.

print(mi_lista)  # Salida: [1, 2, 3, 4] (La lista original ha sido alterada)