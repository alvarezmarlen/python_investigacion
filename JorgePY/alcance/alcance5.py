# Funciones anidadas
# La función b captura la variable x del scope exterior (a), no la global.

x = 1

def a():
    x = 2

    def b():
        print(x)

    b()

a()