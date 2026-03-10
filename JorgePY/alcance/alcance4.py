# x se interpreta como variable local
# se usa antes de asignala
# print(x) imprime error

x = 5

def cambiar():
    x = x + 1

cambiar()
print(x)