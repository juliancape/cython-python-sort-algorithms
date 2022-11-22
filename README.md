# cython-python-sort-algorithms
Comparacion de rendimiento Cython-Python entre algoritmos de ordenamiento bubble sort y selector sort<p>
<b>Problema</b>
Se tiene una lista de numeros decimales entre -1000 y 1000 desorganizada, la cual se requiere organizar, para esta tarea se utilizaran los algoritmos de ordenamiento bubble sort y selector sort,se realizaron tres baterias de experimentos variando el tamaño de la lista:
- 10000 datos
- 20000 datos
- 30000 datos

<b>Bubble sort</b>
Complejidad: O(n^2)
Es un algoritmo de ordenamiento. Funciona revisando cada elemento de la lista que va a ser ordenada con el siguiente, intercambiándolos de posición si están en el orden equivocado. Es necesario revisar varias veces toda la lista hasta que no se necesiten más intercambios, lo cual significa que la lista está ordenada.
<p><b>Selection Sort</b>
Complejidad: O(n^2)
Es un algoritmo de ordenamiento. Su funcionamiento es el siguiente:
<p>1. Buscar el mínimo elemento de la lista
<p>2. Intercambiarlo con el primero
<p>3. Buscar el siguiente mínimo en el resto de la lista
<p>4. Intercambiarlo con el segundo<p>
Se repite hasta llegar al numero mas grande.
