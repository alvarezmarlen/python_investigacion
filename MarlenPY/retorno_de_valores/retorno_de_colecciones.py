# 3. Retorno de Colección: Devuelve estructuras (Listas, Dicts, Conjuntos)
def obtener_usuarios():
  return ["Ana", "Luis", "Marta"]

lista = obtener_usuarios() # Resultado: ['Ana', 'Luis', 'Marta']
print(lista)

# 1. VALOR SIMPLE (Un dato)
def calcular_iva(precio):
    return precio * 0.21
  
total = calcular_iva(100)  
print(total)

# 2. MÚLTIPLES VALORES (Empaquetado en Tupla)
def coordenadas_bilbao():
    return 43.26, -2.93  # Python crea la tupla automáticamente

resultado = coordenadas_bilbao()
print(resultado)


# 3. COLECCIÓN (Datos agrupados)
def sedes_f5():
    return ["Peñascal", "Bolueta", "Madrid"]  # Devuelve una LISTA []
  
lista_sedes = sedes_f5()
print(lista_sedes)

# 4. IMPLÍCITO (Retorno de seguridad)
def mostrar_aviso():
    print("Guardado correctamente") 

# Al no haber 'return', devuelve None
resultado_mostrar = mostrar_aviso()
print(resultado_mostrar)
