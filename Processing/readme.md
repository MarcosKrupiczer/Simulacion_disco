En esta seccion, se realiza el procesado, es decir, se aplica el método de elementos finitos para resolver el problema en cuestión. Esta carpeta contiene los siguientes códigos de Python:

- **funcionesDeForma** define las funciones de forma utilizadas para interpolar las coordenadas globales y las temperaturas de los elementos tetragonales, dadas las coordenadas locales $\eta$, $\xi$, $\tau$
- **derivadasFuncionesDeForma** es una función que devuelve la matriz de derivadas de las funciones de forma respecto de las coordenadas locales/convectivas, dadas estas coordenadas $\eta$, $\xi$, $\tau$
