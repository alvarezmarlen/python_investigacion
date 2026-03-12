#En el paso por valor, el parámetro es una fotocopia (si rayas la copia, el original sigue limpio).
mi_numero = 9  # <--- ARGUMENTO (Dato original)

def doblar_numero(numero): # <--- PARÁMETRO (Recibe la copia)
    return numero * 2

print(doblar_numero(mi_numero)) # (El cálculo sobre la copia)
print(mi_numero)                # (El original está intacto)