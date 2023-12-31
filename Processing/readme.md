# Procesado
En esta seccion, se realiza el procesado, es decir, se aplica el método de elementos finitos para resolver el problema en cuestión. Esta carpeta contiene los siguientes códigos de Python:

- **funcionesDeForma.py**: se definen las funciones de forma utilizadas para interpolar las coordenadas globales y las temperaturas de los elementos tetragonales, dadas las coordenadas locales ($\eta$, $\xi$, $\tau$)
- **derivadasFuncionesDeForma.py**: contiene una función que devuelve la matriz de derivadas de las funciones de forma respecto de las coordenadas locales/convectivas, dadas estas coordenadas ($\eta$, $\xi$, $\tau$)
- **matrizJacobiana.py**: se calcula la matriz jacobiana de la transformación de coordenadas globales ($x$, $y$, $z$) a locales ($\eta$, $\xi$, $\tau$)
- **matrizB.py**: se calcula la matriz gradiente de las funciones de forma, es decir, las derivadas de las funciones de forma respecto de las coordenadas globales ($x$, $y$, $z$)
- **pesosPetrov.py**: se calcula el vector de pesos de Petrov utilizado para estabilizar la solución. Surge de plantear el problema con una formulación Euleriana (con el término convectivo en la ecuación diferencial que da orígen a la matriz convectiva)
- **gauss.py**: se obtienen los pesos y las posiciones de Gauss para un determinado número de puntos de Gauss escogido por el usuario, que puede variar entre 1 y 4
- **matrizMasaLocal.py**: se calcula la matriz de masa de un elemento
- **matrizConvectivaLocal.py**: se calcula la matriz convectiva de un elemento
- **matrizRigidezLocal.py**: se calcula la matriz de rigidez por conducción de un elemento
- **conveccionLocal.py**: se calcula la matriz de rigidez y el vector de calor de un elemento debidos a la condición de borde de convección
- **vectorCalorNeumannLocal.py**: se calcula el vector de calor de un elemento debido a la condición de borde de Neumann (calor generado por la fricción entre la pastilla y el disco de frenos)
- **interseccionListas.py**: se define una función que determina la intersección entre dos listas
- **condicionesDeBorde.py**: se define una función que determina los elementos que pertenecen a las superficies $S\_q$ y $S\_c$, además de los nodos de cada elemento que pertenecen a dichas superficies
- **ensamble.py**: se define una función que ensambla todas las matrices y vectores locales (de cada elemento) para así obtener las matrices y vectores globales
- **coeficienteDeConveccion.py**: se calcula el coeficiente de convección de cada elemento a partir de la correlación de flujo forzado sobre placa plana, utilizando la velocidad de traslación del vehículo
- **parametrosFisicos.py**: se definen los datos físicos y condiciones iniciales del problema (masa del vehículo, coeficiente de Drag, tiempo de frenada, velocidad inicial, etc...)
- **propiedadesAire.py**: se definen las propiedades como la conductividad térmica y la viscosidad cinemática del aire en función de su temperatura
- **propiedadesDisco.py**: se definen las propiedades como la conductividad térmica y el producto de la densidad por el calor específico del material del disco (fundición gris) en función de su temperatura
- **resolucionNumerica.py**: se definen los parámetros numéricos (como pasos temporales) y se resuelve el sistema no lineal de ecuaciones utilizando los métodos de Picard y Crank-Nicholson

Se adjuntan además, imágenes de los gráficos de las propiedades relevantes del aire y de la fundición gris del disco en función de la temperatura: **prop_aire.png** y **prop_disco.png**

Se muestra también una imágen del diagrama de flujo representativo del algoritmo utilizado en el código **resolucionNumerica.py**: **flujo.png**
