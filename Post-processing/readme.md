En esta sección, se realiza el post-procesado, es decir, el tratamiento y la visualización de los resultados.
Se tienen los archivos siguientes:
- **preparacion.py**: se redefine la matriz de coordenadas de los nodos (como en el pre-processing), se cargan los resultados (que fueron grabados en archivos de texto en el procesado) y se determinan las temperaturas mínima y máxima
- **videos.py**: se graban videos de una vista en perpectiva del disco, donde se muestra la evolución temporal de la temperatura en todo el volumen del disco
- **cortes.py**: se generan figuras de cortes verticales y horizontales del disco, donde se muestran las temperaturas para ciertos instantes de tiempo
- **plots**: se grafica la temperatura en función de la coordenada pseudo-radial (coordenada radial que tiene en cuenta el cambio de espesor)
