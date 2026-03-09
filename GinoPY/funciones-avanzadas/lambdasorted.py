# Ejemplo de función lambda con sorted en Python
# sorted() ordena un iterable, y podemos usar lambda para definir el criterio de ordenación

# Lista de diccionarios que representan estudiantes
estudiantes = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Juan", "nota": 6},
    {"nombre": "Pedro", "nota": 10}
]

# Ordenamos la lista de diccionarios por la clave 'nota' usando una lambda
# sorted(iterable, key=función_de_clave)
# lambda x: x['nota'] toma cada diccionario (x) y devuelve el valor de su nota para comparar
estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['nota'])

# Imprimimos el resultado ordenado
print("Estudiantes ordenados por nota:")
for estudiante in estudiantes_ordenados:
    print(f"{estudiante['nombre']}: {estudiante['nota']}")
