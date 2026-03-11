# 4. Retorno Implícito: La función termina sin 'return', devuelve None
def saludar(nombre):
  print(f"Hola, {nombre}")    # Al no haber return, Python añade implícitamente: return None

resultado_saludo = saludar("Juan") # Resultado: None
print(resultado_saludo)