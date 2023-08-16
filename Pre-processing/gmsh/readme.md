# GMSH
En esta carpeta se adjuntan capturas con los pasos a seguir para mallar el disco con el software gmsh.
1. Importar el archivo **.step** de la geometría (se debe ver una pantalla como la de la imágen **gmsh1.png**)
2. Unir ambos volúmenes (**gmsh2.png**)
3. Definir los **Physical Groups** (**gmsh3.png**)
   - *neumann*: superficie $S\_q$ donde se genera el calor por fricción
   - *conveccion*: superficie $S\_c$ expuesta al aire exterior
   - *aislado*: superficies que se consideran aisladas térmicamente
   - *dominio*: volumen del disco (esfera amarilla)
4. Definir las condiciones y parámetros de mallado (**gmsh4.png**)
5. Realizar mallado (**gmsh5.png**)
6. Chequear información de la malla, en particular, el número de elementos tetragonales y triangulares (**gmsh6.png**)
Finalmente, exportar la malla para obtener el archivo **disco.msh**
