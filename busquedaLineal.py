import time

def busquedaLineal(lista, obj):
    for i in range(len(lista)):
        if lista[i] == obj:
            return i
    return -1

lista = [13, 2, 39, 1, 5, 15, 27, 6, 50, 3, 7, 20, 10, 34, 9, 11, 45, 18, 22, 8, 25, 14, 30, 4, 12, 17, 28, 33, 16, 21, 36, 19, 24, 29, 35, 40, 23, 26, 31, 37, 41, 42, 32, 38, 43, 44, 46, 47, 48, 49]
buscar = 13

inicio = time.perf_counter()
resultado = busquedaLineal(lista, buscar)
fin = time.perf_counter()

tiempo_ms = (fin - inicio) * 1000

if resultado != -1:
    print(f"El número {buscar} se encuentra en la posición: {resultado}")
else:
    print(f"El número {buscar} no se encuentra en la lista.")

print(f"Tiempo de ejecución: {tiempo_ms:.5f} ms")