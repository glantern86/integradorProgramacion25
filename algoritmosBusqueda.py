import time
    
def busquedaLineal(lista, obj):
    for i in range(len(lista)):
        if lista[i] == obj:
            return i
    return -1

def busquedaBinaria(lista, objetivo, inicio, fin):
    if inicio > fin:
        return -1

    centro = (inicio + fin) // 2
    if lista[centro] == objetivo:
        return centro
    elif lista[centro] < objetivo:
        return busquedaBinaria(lista, objetivo, centro + 1, fin)
    else:
        return busquedaBinaria(lista, objetivo, inicio, centro - 1)

lista = list(range(1, 100001))
numero_objetivo = 50000


inicio_binaria = time.perf_counter()
resultado_binaria = busquedaBinaria(lista, numero_objetivo, 0, len(lista) - 1)
fin_binaria = time.perf_counter()
tiempo_binaria = (fin_binaria - inicio_binaria) * 1000


inicio_lineal = time.perf_counter()
resultado_lineal = busquedaLineal(lista, numero_objetivo)
fin_lineal = time.perf_counter()
tiempo_lineal = (fin_lineal - inicio_lineal) * 1000


print(f"[Búsqueda Lineal ] El número {numero_objetivo} se encuentra en la posición real: {resultado_lineal+1}, Tiempo: {tiempo_lineal:.5f} ms")
print(f"[Búsqueda Binaria] El número {numero_objetivo} se encuentra en la posición real: {resultado_binaria+1}, Tiempo: {tiempo_binaria:.5f} ms")

