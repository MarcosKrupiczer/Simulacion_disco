En esta seccion, se realiza el procesado, es decir, se aplica el método de elementos finitos para resolver el problema en cuestión. Esta carpeta contiene los siguientes códigos de Python:

- **funcionesDeForma**: se definen las funciones de forma utilizadas para interpolar las coordenadas globales y las temperaturas de los elementos tetragonales, dadas las coordenadas locales ($\eta$, $\xi$, $\tau$)
- **derivadasFuncionesDeForma**: contiene una función que devuelve la matriz de derivadas de las funciones de forma respecto de las coordenadas locales/convectivas, dadas estas coordenadas ($\eta$, $\xi$, $\tau$)
- **matrizJacobiana**: se calcula la matriz jacobiana de la transformación de coordenadas globales ($x$, $y$, $z$) a locales ($\eta$, $\xi$, $\tau$)
- **matrizB**: se calcula la matriz gradiente de las funciones de forma, es decir, las derivadas respecto de las coordenadas globales ($x$, $y$, $z$)
- 
