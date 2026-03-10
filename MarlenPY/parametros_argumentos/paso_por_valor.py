""" En el paso por valor, el parámetro es una fotocopia (si rayas la copia, el original sigue limpio)."""

def doblar_numero(numero):
    numero = numero * 2
    return numero

# variable original
mi_numero = 3

# Llamada y Salida
print(doblar_numero(mi_numero))


print (mi_numero)