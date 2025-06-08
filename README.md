# Integrador Programación I

Repositorio público para el trabajo integrador de Programación I.

Integrante: Prados Gonzalo

# Introducción

Este trabajo pretende ser un primer acercamiento a los algoritmos de búsqueda y ordenamiento: cómo funcionan, cuáles son los más efectivos y en qué momentos conviene usar uno u otro.

Cuando hablamos de algoritmos de búsqueda, hablamos de una serie de instrucciones detalladas para poder retirar o adquirir cierta información dentro de una estructura de datos. Los algoritmos de ordenamiento, por otro lado, son una serie de instrucciones para imponer orden dentro de una serie, grupo o conjunto. Una búsqueda efectiva implica mejores tiempos de respuesta y una mejor optimizacion del tiempo de cómputo.

En este trabajo nos vamos a enfocar en las dos formas más primitivas de estos algoritmos: la búsqueda lineal y la búsqueda binaria. Hablo de formas primitivas porque claramente hay formas más avanzadas y complejas, pero estas sientan las bases conceptuales y fundamentos de esas otras formas.

# Marco Teórico

## Búsqueda Lineal

Los algoritmos de búsqueda lineal, también conocidos como búsqueda secuencial, implican recorrer una lista de elementos uno por uno hasta encontrar un elemento específico. Este algoritmo es muy sencillo de implementar en código y extremadamente intuitivo, pero puede ser muy ineficiente dependiendo del largo de la lista y la ubicación donde se encuentra el elemento. 

Las ventajas principales de este tipo de búsqueda son su sencillez y su flexibilidad. Por un lado, la búsqueda lineal es uno de los algoritmos más simples y fáciles de implementar y solo requiere iterar a través de la lista de elementos uno por uno hasta encontrar el objetivo. También puede aplicarse a cualquier tipo de lista, independientemente de si está ordenada o no.

Sus desventajas radican en su ineficiencia al manejar grandes volúmenes de datos y en que no es el método óptimo para listas ordenadas. La búsqueda lineal es extremadamente ineficiente en listas grandes, ya que compara cada elemento uno por uno, lo cual implica que su tiempo de ejecución crezca de manera lineal con el tamaño de la lista. La otra dificultad es que aunque puede funcionar en listas no ordenadas, no es particularmente eficiente para listas ordenadas, en esos casos es muchas veces preferible la busqueda binaria.

## Búsqueda Binaria

El algoritmo de búsqueda binaria es un algoritmo muy eficiente que se aplica solo a listas ordenadas. Funciona dividiendo repetidamente la lista en dos mitades y comparando el elemento objetivo con el elemento del medio. Esto reduce dramáticamente la cantidad de comparaciones necesarias.

Las dos ventajas principales de este método son su eficiencia y su reducido número de comparaciones. Su tiempo de ejecución es de O(log n), lo que significa que disminuye rápidamente a medida que el tamaño de la lista aumenta. Comparado con la búsqueda lineal, la búsqueda binaria realiza menos comparaciones en promedio, lo que la hace más rápida para encontrar el objetivo.

Su desventaja principal es que requiere una lista ordenada y en segundo lugar que acarrea una mayor complejidad a la hora de la implementación. Si la lista no está ordenada, se debe realizar una operación adicional para ordenarla antes de usar este método, lo cual implica un costoa dicional de cómputo. Comparado con la búsqueda lineal, la búsqueda binaria también es más compleja de implementar debido a su naturaleza recursiva.

# Caso Práctico

## ESCENARIO 1

Para este caso de estudio vamos a hacer la comparativa entre ambos algoritmos utilizando una lista desordenada. Puesto que la búsqueda binaria no funciona con listas desordenadas, vamos a tener que aplicar el método `.sort()` y pagar el tiempo de cómputo correspondiente. También estoy utilizando el módulo `time` para poder medir cuánto tiempo tarda cada llamada.

**Búsqueda Lineal**

Acá presentamos un algoritmo de búsqueda lineal extremadamente simple en Python (también disponible en el repositorio bajo el nombre `busquedaLineal.py`).  
Nuestro código se limita a buscar un número en una lista y nos devuelve la posición en la que se encuentra el número. Ya sea que se encuentre o no el número deseado, nos devuelve un mensaje con el resultado de la búsqueda. Comencé por definir la función principal, el código lo que hace es ir elemento por elemento de la lista hasta que encuentra el que estamos buscando. Para este primer escenario vamos a buscar el número 26, que se encuentra en la posición 37 de una lista que contiene 50 elementos.

```python
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
```

Resultado Búsqueda Lineal:

```
El número 26 se encuentra en la posición: 37
Tiempo de ejecución: 0.01136 ms
```

**Búsqueda Binaria**

Este es nuestro algoritmo de búsqueda binaria (también disponible en el repositorio bajo el nombre `busquedaBinaria.py`).  
En este código implementamos la búsqueda binaria de forma recursiva. Primero ordenamos la lista luego vamos dividiendo el rango de búsqueda a la mitad comparando el valor del medio con el número buscado. Esto permite encontrar el elemento rápidamente en listas ordenadas, con un menor número de comparaciones que la búsqueda lineal.

```python
import time

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

lista = [13, 2, 39, 1, 5, 15, 27, 6, 50, 3, 7, 20, 10, 34, 9, 11, 45, 18, 22, 8, 25, 14, 30, 4, 12, 17, 28, 33, 16, 21, 36, 19, 24, 29, 35, 40, 23, 26, 31, 37, 41, 42, 32, 38, 43, 44, 46, 47, 48, 49]
lista.sort()
numero_objetivo = 13
inicio_busqueda = 0
fin_busqueda = len(lista) - 1

inicio = time.perf_counter()
resultado = busquedaBinaria(lista, numero_objetivo, inicio_busqueda, fin_busqueda)
fin = time.perf_counter()

tiempo_ms = (fin - inicio) * 1000

if resultado != -1:
    print(f"El número {numero_objetivo} se encuentra en la posición {resultado}.")
else:
    print(f"El número {numero_objetivo} NO se encuentra en la lista.")

print(f"Tiempo de ejecución: {tiempo_ms:.5f} ms")
```

Resultado Búsqueda Binaria:

```
El número 26 se encuentra en la posición 25.
Tiempo de ejecución: 0.00659 ms
```

## ESCENARIO 2

El segundo escenario voy a plantearlo con el número 13, el cual se encuentra en la posición 0, y por una cuestión de simpleza, solamente voy a copiar los resultados.

Resultado Búsqueda Lineal:

```
El número 13 se encuentra en la posición: 0
Tiempo de ejecución: 0.00633 ms
```

Resultado Búsqueda Binaria:

```
El número 13 se encuentra en la posición 12.
Tiempo de ejecución: 0.01236 ms
```

# Metodología Utilizada

La metodología incluye una investigación exhaustiva en diversas fuentes, presentes en la seccion de Bibliografía. Luego procedí a generar algoritmos de prueba para verificar de forma empírica los tiempos de cómputo y compararlos.  
Como herramienta de trabajo estoy utilizando Visual Studio Code como IDE, GitHub Copilot para ayudarme a corregir mi código y GitHub como plataforma en la que voy a publicar mi trabajo.  
Incluyo el módulo `time` para poder medir los tiempos de ejecución y el método `sort` para ordernar mi lista.

# Resultados Obtenidos

A primera vista salta el hecho de la longitud del código. Mientras que nuestro algoritmo de búsqueda lineal tiene 23 líneas, el de búsqueda binaria tiene 32, casi un 40% más de código. Respecto de que la búsqueda lineal es más simple, no hay duda alguna.

Respecto al tiempo de cómputo, estamos analizando primero un escenario que es beneficioso para la búsqueda binaria. Tomamos una serie de 50 elementos y el elemento que buscamos está por más de la mitad (en la posición 37 de 50). Mientras que la búsqueda lineal demora 0.01136 ms, la binaria demora 0.00659 ms casi la mitad del tiempo.

En el segundo escenario analizamos un caso que es extremadamente provechoso para la búsqueda lineal. El elemento a buscar es el primero de la serie. Mientras que la búsqueda lineal demora 0.00633 ms, la binaria está tardando 0.01236 ms.


# Conclusión Final

La busqueda lineal y la busqueda binaria son elementos extremadamente básicos pero no dejan de ser utiles en ciertos contextos. Si estamos hablando de listas de pocos elementos desordenados la busqueda lineal es una buena opcion de implementar, sin embargo su rendimiento decrece de forma drástica a medida que los elementos de la lista van creciendo o el elemento en cuestion se encuentra al final de la lista. La búsqueda binaria demuestra ser mucho más eficiente en listas ordenadas, reduciendo el tiempo de búsqueda gracias a la estrategia de divide y conquistarás. No obstante, requiere que la lista esté ordenada previamente, lo cual puede implicar un costo computacional extra.

Los resultados de mi investigación arrojan que la búsqueda lineal es una buena opción para volumenes pequeños de datos pero que la busqueda binaria es la más eficiente a medida que se van agregando elementos en la lista. Comparativamente hablando ambos algoritmos tienen sus fortalezas y debilidades, ninguno es ampliammente superior al otro ni ninguno deja al otro obsoleto sino que es el contexto el que prima en estas ocasiones. Ambas son herramientas útiles en el repertorio de todo desarrollador.
	
# Bibliografía
Algoritmos de Ordenamiento y Búsqueda en Python: Optimizando la Gestión de Datos. (2025, April 25). 4Geeks. [https://4geeks.com/es/lesson/algoritmos-de-ordenamiento-y-busqueda-en-python](https://4geeks.com/es/lesson/algoritmos-de-ordenamiento-y-busqueda-en-python)

Krishna, A. (2024, August 14). Search algorithms – linear search and binary search code implementation and complexity analysis. freeCodeCamp.org. [https://www.freecodecamp.org/news/search-algorithms-linear-and-binary-search-explained/](https://www.freecodecamp.org/news/search-algorithms-linear-and-binary-search-explained/)

TutorialsPoint. (2025, March 25). Searching algorithms. [https://www.tutorialspoint.com/data_structures_algorithms/searching_algorithms.htm](https://www.tutorialspoint.com/data_structures_algorithms/searching_algorithms.htm)

TutorialsPoint. (2025a, March 25). Linear Search Algorithm. [https://www.tutorialspoint.com/data_structures_algorithms/linear_search_algorithm.htm](https://www.tutorialspoint.com/data_structures_algorithms/linear_search_algorithm.htm)

TutorialsPoint. (2025a, March 25). Binary search algorithm. [https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm](https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm)
