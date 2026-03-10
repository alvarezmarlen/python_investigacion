# Uso de global
# Incrementar() modifica una variable global
# print(contador) imprime 2

contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
print(contador)