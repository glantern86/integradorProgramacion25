# Integrador Programacion I
Repositorio publico para el trabajo integrador de Programación I

# Introducción
Los algoritmos de busqueda son una serie de instrucciones detalladas para poder retirar o adquirir cierta informacion dentro de una estructura de datos. Los algoritmos de ordenamiento por otro lado son una serie de instrucciones para imponer orden dentro una serie, grupo o conjunto. La importancia de ambas es evidente dentro del marco de la era en la que vivimos: la era de la información.

Vivimos en un mundo en el que el acceso a la informacion no es un problema sino su calidad. Teniendo esto en cuesta la efectividad la hora de realizar busquedas y ordenar los resultados es de importancia capital.

En este trabajo nos vamos a enfocar en las dos formas más primitvas de ambos. La búsqueda lineal y la búsqueda bonaria. Hablo de formas primitivas porque claramente hay formas mas avanzadas de búsqueda y complejas pero estas sientan las bases conceptuales y fundamentos de esas otras formas. 

# Marco Teórico

## Busqueda Lineal
Los algoritmos de búsqueda lineal, también conocidos como búsqueda secuencial, implican recorrer una lista de elementos uno por uno hasta encontrar un elemento específico. Este algoritmo es muy sencillo de implementar en código pero puede ser muy ineficiente dependiendo del largo de la lista y la ubicación donde está el elemento. Es un algoritmo extremadamente sencillo e intuitivo 

Dos ventajas de éste tipo de búsqueda son su snecillez y su flexibilidad. Por un lado la búsqueda lineal es uno de los algoritmos de búsqueda más simples y fáciles de implementar y solo requiere iterar a través de la lista de elementos uno por uno hasta encontrar el objetivo. Tambien puede aplicarse a cualquier tipo de lista, independientemente de si está ordenada o no.

Su deventajas son su ineficiencia a la hora de manejar grandes volumenes de datos y que no es el método óptimo para manejar listas ordenadas.La búsqueda lineal es extremadamente ineficiente en listas grandes ya que compara cada elemento uno por uno lo cual implica que su tiempo de ejecución crezca de manera lineal con el tamaño de la lista. La otra dificultad es que aunque puede funcionar en listas no ordenadas, la búsqueda lineal no es eficiente para listas ordenadas. En tales casos, algoritmos de búsqueda más eficientes, como la búsqueda binaria, son preferibles.

## Búsqueda Binaria
El algoritmo de búsqueda binaria es un algoritmo muy eficiente que se aplica solo a listas ordenadas. Funciona dividiendo repetidamente la lista en dos mitades y comparando el elemento objetivo con el elemento del medio, esto reduce dramaticamente la cantidad de comparaciones necesarias.

Las dos ventajas principales de éste método son su eficiencia en listas ordenadas y su reducido numero de comparaciones. Su tiempo de ejecución es de O(log n), lo que significa que disminuye rápidamente a medida que el tamaño de la lista aumenta. Comparado con la búsqueda lineal, la búsqueda binaria realiza menos comparaciones en promedio, lo que lo hace más rápido para encontrar el objetivo.

Sus desventajas son que requiere una lista ordenada y que acarrea una mayor complejidad a la hora de la implementacion. Si la lista no está ordenada, se debe realizar una operación adicional para ordenarla antes de usar éste método. Comparado con la búsqueda lineal, la búsqueda binaria es más compleja de implementar debido a su naturaleza recursiva.

# Caso Practico
# Metodología Utilizada	
# Resultados Obtenidos	
# Conclusión Final	
# Bibliografía
Algoritmos de Ordenamiento y Búsqueda en Python: Optimizando la Gestión de Datos. (2025, April 25). 4Geeks. [https://4geeks.com/es/lesson/algoritmos-de-ordenamiento-y-busqueda-en-python](https://4geeks.com/es/lesson/algoritmos-de-ordenamiento-y-busqueda-en-python)

Krishna, A. (2024, August 14). Search algorithms – linear search and binary search code implementation and complexity analysis. freeCodeCamp.org. [https://www.freecodecamp.org/news/search-algorithms-linear-and-binary-search-explained/](https://www.freecodecamp.org/news/search-algorithms-linear-and-binary-search-explained/)

TutorialsPoint. (2025, March 25). Searching algorithms. [https://www.tutorialspoint.com/data_structures_algorithms/searching_algorithms.htm](https://www.tutorialspoint.com/data_structures_algorithms/searching_algorithms.htm)

TutorialsPoint. (2025a, March 25). Linear Search Algorithm. [https://www.tutorialspoint.com/data_structures_algorithms/linear_search_algorithm.htm](https://www.tutorialspoint.com/data_structures_algorithms/linear_search_algorithm.htm)

TutorialsPoint. (2025a, March 25). Binary search algorithm. [https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm](https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm.htm)

# Anexos



-------------
## Datacamp Python:

```

La búsqueda lineal no necesita que los datos estén ordenados para funcionar, por lo que se utiliza principalmente en conjuntos de datos sin ordenar. Esto lo hace útil en situaciones en las que no es práctico ordenar, o cuando trabajas con datos en bruto. Sin embargo, esta ventaja tiene un coste: no es tan eficaz como otros algoritmos que requieren datos preclasificados.

La búsqueda lineal es ideal en situaciones en las que trabajas con conjuntos de datos relativamente pequeños o cuando ordenar los datos no es factible. El diagrama siguiente ofrece una explicación simplificada.

## ¿Por qué elegir la búsqueda lineal?
En mi opinión, la búsqueda lineal tiene tres ventajas distintas:

Cuando la clave es la sencillez
Una de las mayores ventajas de la búsqueda lineal es su sencillez. El algoritmo es fácil de entender y aplicar. No hay que preocuparse de complejas ordenaciones o divisiones de los datos. Simplemente empieza por el principio de la lista y comprueba cada elemento hasta que encuentres lo que buscas.

Cuando no tienes tiempo para ordenar
A diferencia de otros algoritmos de búsqueda, como la búsqueda binaria, la búsqueda lineal no requiere que el conjunto de datos esté ordenado. Esto lo hace perfecto para cuando necesites encontrar algo rápidamente.

Cuando necesitas versatilidad
Otra ventaja de la búsqueda lineal es que es versátil. No sólo funciona con matrices, sino también con otras estructuras de datos de Python, como las listas enlazadas. Mientras puedas acceder secuencialmente a los elementos, la búsqueda lineal puede hacer el trabajo. Es lo suficientemente flexible como para manejar distintos tipos de datos, desde números a cadenas, e incluso objetos.

¿Por qué pensar dos veces en la búsqueda lineal?
Hay una cuestión a tener en cuenta:

Cuando la eficiencia importa
El principal inconveniente de la búsqueda lineal es su ineficacia, especialmente con grandes conjuntos de datos. Su complejidad temporal es O(n), lo que significa que, en el peor de los casos, ¡tendrías que comprobar cada uno de los elementos de la lista! Esto puede ralentizar mucho las cosas si trabajas con miles o millones de entradas. Sin embargo, para conjuntos de datos pequeños, esta ineficacia puede ser insignificante.

## Búsqueda lineal vs. Otros algoritmos de búsqueda
La búsqueda lineal es sólo uno de los muchos algoritmos de búsqueda que existen. Veamos otros dos algoritmos de búsqueda habituales: la búsqueda binaria y la búsqueda hash.

Búsqueda lineal vs. búsqueda binaria
La búsqueda binaria es un algoritmo que encuentra la posición de un valor objetivo dentro de una matriz ordenada dividiendo repetidamente el intervalo de búsqueda por la mitad. Tiene una complejidad temporal de O(log n), lo que la hace mucho más eficaz que la búsqueda lineal. Sin embargo, sólo funciona con datos ordenados. Cuando tu conjunto de datos está ordenado, la búsqueda binaria es casi siempre la mejor opción, porque reduce el espacio de búsqueda a la mitad en cada paso, reduciendo drásticamente el número de comparaciones necesarias para encontrar el objetivo.

La búsqueda lineal puede ser más adecuada en situaciones en las que tus datos no estén ordenados, ya que la búsqueda lineal funciona en cualquier conjunto de datos, ordenado o no. Sin embargo, con una complejidad temporal de O(n), la búsqueda lineal es mucho menos eficiente en conjuntos de datos ordenados.

Búsqueda lineal vs. búsqueda hash
La búsqueda hash es un método que utiliza una tabla hash para encontrar rápidamente un elemento. Con una complejidad temporal de O(1), es significativamente más rápido que la búsqueda lineal o binaria. Sin embargo, esta velocidad tiene un coste: primero tienes que construir una tabla hash, lo que requiere tiempo y memoria adicional. Las búsquedas Hash funcionan mejor cuando necesitas buscar en grandes conjuntos de datos varias veces, de modo que la configuración inicial compense con el tiempo.

En cambio, la búsqueda lineal no requiere configuración, por lo que es una opción más sencilla. Es la mejor opción cuando sólo necesitas buscar una vez o unas pocas veces, donde el tiempo extra para configurar una tabla hash no está justificado. La búsqueda lineal también puede ocupar menos espacio porque no necesitas almacenar una tabla hash para utilizar el algoritmo.
```


