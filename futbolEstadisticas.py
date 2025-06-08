# Lista de jugadores
jugadores = [
    {"nombre": "Messi", "goles": 30, "fouls": 5, "asistencias": 12},
    {"nombre": "Ronaldo", "goles": 25, "fouls": 3, "asistencias": 9},
    {"nombre": "Mbappé", "goles": 28, "fouls": 7, "asistencias": 14},
    {"nombre": "Neymar", "goles": 15, "fouls": 8, "asistencias": 20},
    {"nombre": "Haaland", "goles": 35, "fouls": 6, "asistencias": 4},
    {"nombre": "Lewandowski", "goles": 26, "fouls": 4, "asistencias": 7},
    {"nombre": "Benzema", "goles": 22, "fouls": 2, "asistencias": 10},
    {"nombre": "Vinicius", "goles": 18, "fouls": 5, "asistencias": 11},
    {"nombre": "Modric", "goles": 6, "fouls": 1, "asistencias": 13},
    {"nombre": "De Bruyne", "goles": 10, "fouls": 3, "asistencias": 18},
    {"nombre": "Griezmann", "goles": 14, "fouls": 6, "asistencias": 12},
    {"nombre": "Kane", "goles": 27, "fouls": 4, "asistencias": 5},
    {"nombre": "Salah", "goles": 21, "fouls": 3, "asistencias": 8},
    {"nombre": "Mané", "goles": 19, "fouls": 2, "asistencias": 6},
    {"nombre": "Sancho", "goles": 13, "fouls": 2, "asistencias": 9},
    {"nombre": "Foden", "goles": 11, "fouls": 3, "asistencias": 10},
    {"nombre": "Pedri", "goles": 5, "fouls": 1, "asistencias": 14},
    {"nombre": "Gavi", "goles": 4, "fouls": 2, "asistencias": 11},
    {"nombre": "Bellingham", "goles": 12, "fouls": 3, "asistencias": 7},
    {"nombre": "Álvarez", "goles": 16, "fouls": 4, "asistencias": 6},
    {"nombre": "Di María", "goles": 9, "fouls": 2, "asistencias": 13},
    {"nombre": "Vlahovic", "goles": 17, "fouls": 5, "asistencias": 4},
    {"nombre": "Oshimen", "goles": 23, "fouls": 6, "asistencias": 3},
    {"nombre": "João Félix", "goles": 8, "fouls": 2, "asistencias": 9},
    {"nombre": "Zlatan", "goles": 7, "fouls": 3, "asistencias": 2}
]


# Función para obtener jugador con más de un campo
def jugador_con_mas(jugadores, campo):
    mayor = jugadores[0]
    for jugador in jugadores:
        if jugador[campo] > mayor[campo]:
            mayor = jugador
    return mayor

# Función para obtener jugador con menos de un campo
def jugador_con_menos(jugadores, campo):
    menor = jugadores[0]
    for jugador in jugadores:
        if jugador[campo] < menor[campo]:
            menor = jugador
    return menor

# Función para ordenar por un campo
def ordenar_jugadores(jugadores, campo, descendente=True):
    copia = jugadores[:]
    for i in range(len(copia)):
        for j in range(i + 1, len(copia)):
            if descendente:
                if copia[i][campo] < copia[j][campo]:
                    temp = copia[i]
                    copia[i] = copia[j]
                    copia[j] = temp
            else:
                if copia[i][campo] > copia[j][campo]:
                    temp = copia[i]
                    copia[i] = copia[j]
                    copia[j] = temp
    return copia

# Función para ordenar alfabéticamente por nombre (para búsqueda binaria)
def ordenar_por_nombre(jugadores):
    copia = jugadores[:]
    for i in range(len(copia)):
        for j in range(i + 1, len(copia)):
            if copia[i]["nombre"].lower() > copia[j]["nombre"].lower():
                temp = copia[i]
                copia[i] = copia[j]
                copia[j] = temp
    return copia

# Búsqueda binaria por nombre (requiere lista ordenada)
def buscar_jugador_por_nombre(jugadores_ordenados, nombre):
    izquierda = 0
    derecha = len(jugadores_ordenados) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = jugadores_ordenados[medio]["nombre"].lower()
        if actual == nombre.lower():
            return jugadores_ordenados[medio]
        elif actual < nombre.lower():
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

# Mostrar todos los jugadores
def mostrar_lista(jugadores):
    for j in jugadores:
        print("Nombre:", j["nombre"], "- Goles:", j["goles"], "- Fouls:", j["fouls"], "- Asistencias:", j["asistencias"])

# Menú principal
if __name__ == "__main__":
    print("Estadísticas de jugadores de fútbol")
    print("1. Mostrar jugador con más goles")
    print("2. Mostrar jugador con menos fouls")
    print("3. Ordenar por asistencias")
    print("4. Mostrar todos los jugadores")
    print("5. Buscar jugador por nombre (búsqueda binaria)")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        j = jugador_con_mas(jugadores, "goles")
        print("Jugador con más goles:", j["nombre"], "(", j["goles"], "goles)")
    elif opcion == "2":
        j = jugador_con_menos(jugadores, "fouls")
        print("Jugador con menos fouls:", j["nombre"], "(", j["fouls"], "fouls)")
    elif opcion == "3":
        ordenados = ordenar_jugadores(jugadores, "asistencias", descendente=False)
        print("Jugadores ordenados por asistencias (menor a mayor):")
        mostrar_lista(ordenados)
    elif opcion == "4":
        print("Lista completa de jugadores:")
        mostrar_lista(jugadores)
    elif opcion == "5":
        nombre = input("Ingrese el nombre del jugador a buscar: ")
        jugadores_ordenados = ordenar_por_nombre(jugadores)
        resultado = buscar_jugador_por_nombre(jugadores_ordenados, nombre)
        if resultado:
            print("Jugador encontrado:", resultado["nombre"])
            print("Goles:", resultado["goles"], "- Fouls:", resultado["fouls"], "- Asistencias:", resultado["asistencias"])
        else:
            print("Jugador no encontrado.")
    else:
        print("Opción inválida.")
