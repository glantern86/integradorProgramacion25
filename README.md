# Integrador Programacion I
Repositorio publico para el trabajo integrador de Programación I

'Acá estoy poniendo info que creo que es interesante, primero pongo la fuente y luego el texto que me interesa. La intención es despues poder volver a los textos y que sea mas simple la investigación' 

## Free Code Camp: 
[Free Code Camp Link](https://www.freecodecamp.org/news/search-algorithms-linear-and-binary-search-explained/)

## 4Geeks: 
[4Geeks Link](https://4geeks.com/es/lesson/algoritmos-de-ordenamiento-y-busqueda-en-python)
```
## Búsqueda Lineal
Los algoritmos de búsqueda lineal, también conocidos como búsqueda secuencial, implican recorrer una lista de elementos uno por uno hasta encontrar un elemento específico. Este algoritmo es muy sencillo de implementar en código pero puede ser muy ineficiente dependiendo del largo de la lista y la ubicación donde está el elemento. A continuación veremos un pequeño ejemplo de código en Python.

En este ejemplo de código, necesitamos buscar el número 39, para buscarlo de forma lineal simplemente recorremos la lista con la ayuda de una estructura de bucle for y luego preguntamos si el elemento actual es igual a el elemento que estamos buscando, de ser así retornamos el índice del elemento y terminamos el bucle pero si el bucle termina y no retorno ningún elemento significa que el número que buscamos no se encuentra en la lista por lo que retornamos -1. Este algoritmo puede ser útil para recorrer listas pequeñas o listas desordenadas pero no es eficiente para recorrer listas demasiado largas.

## Ventajas y Desventajas del Algoritmo de Búsqueda Lineal
## Ventajas:
Sencillez: La búsqueda lineal es uno de los algoritmos de búsqueda más simples y fáciles de implementar. Solo requiere iterar a través de la lista de elementos uno por uno hasta encontrar el objetivo.
flexibilidad: La búsqueda lineal puede aplicarse a cualquier tipo de lista, independientemente de si está ordenada o no.
## Desventajas:
Ineficiencia en listas grandes: La principal desventaja de la búsqueda lineal es su ineficiencia en listas grandes. Debido a que compara cada elemento uno por uno, su tiempo de ejecución crece de manera lineal con el tamaño de la lista.
No es adecuada para listas ordenadas: Aunque puede funcionar en listas no ordenadas, la búsqueda lineal no es eficiente para listas ordenadas. En tales casos, algoritmos de búsqueda más eficientes, como la búsqueda binaria, son preferibles.


## Búsqueda Binaria
El algoritmo de búsqueda binaria es un algoritmo muy eficiente que se aplica solo a listas ordenadas. Funciona dividiendo repetidamente la lista en dos mitades y comparando el elemento objetivo con el elemento del medio, esto reduce significativamente la cantidad de comparaciones necesarias.

A continuación veremos un pequeño ejemplo de búsqueda binaria con Python.
En este ejemplo, hacemos uso de un algoritmo de búsqueda binario para encontrar el número 27 en una lista de elementos ordenados, para poder encontrar el elemento que buscamos podemos hacer uso de una función recursiva, en esta función el caso base sería si el número de la lista en la posición centro es igual al número que buscamos, de ser así retornamos el valor de la variable centro este sería el índice del número, de lo contrario, dividimos la lista en dos mitades y hacemos el llamado recursivo hasta encontrar el número que buscamos pero si el número no se encuentra en la lista retornamos -1.

## Ventajas y Desventajas del Algoritmo de Búsqueda Binaria
## Ventajas:
Eficiencia de listas ordenadas: La principal ventaja de la búsqueda binaria es su eficiencia en listas ordenadas. Su tiempo de ejecución es de O(log n), lo que significa que disminuye rápidamente a medida que el tamaño de la lista aumenta.
Menos comparaciones: Comparado con la búsqueda lineal, la búsqueda binaria realiza menos comparaciones en promedio, lo que lo hace más rápido para encontrar el objetivo.
## Desventajas:
Requiere una lista ordenada: La búsqueda binaria sólo es aplicable a listas ordenadas, Si la lista no está ordenada, se debe realizar una operación adicional para ordenarla antes de usar la búsqueda binaria.
Mayor complejidad de implementación: Comparado con la búsqueda lineal, la búsqueda binaria es más compleja de implementar debido a su naturaleza recursiva.
```
-------------
## Datacamp Python:
[Datacamp Python Link](https://www.datacamp.com/es/tutorial/linear-search-python)
```
La búsqueda lineal es un algoritmo que localiza un valor concreto dentro de una lista comprobando cada elemento uno a uno. Empieza por el primer elemento, lo compara con el objetivo y sigue moviéndose por la lista hasta que encuentra el objetivo o llega al final de la lista. Es un algoritmo sencillo e intuitivo.

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


