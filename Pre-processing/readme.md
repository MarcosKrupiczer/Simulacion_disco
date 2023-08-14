# Pre-procesado
Esta carpeta contiene los datos del pre-procesado. 
- **gmsh**: carpeta donde se detalla el uso del software [gmsh](https://gmsh.info/) para el mallado
- **disco.step**: archivo de geometría generado mediante el software de modelado 3D [Onshape](https://cad.onshape.com/documents/0aa5e16aa5ecf79ffe00628e/w/097ac0cb551f4c448e337ade/e/b8136df38db1e787394d104c?renderMode=0&uiState=64d9410fc1a6b3592a9654ca)
- **disco.geo**: archivo de geometría generado por el software de mallado gmsh
- **disco.msh**: archivo del mallado generado por el gmsh
- **preProcessing.py**: código de Python que trata los datos del mallado y genera las matrices necesarias para el procesado
- **3d.png**: imágen mostrando la geometría del disco y señalando las superficies donde se aplicarán las condiciones de borde
- **malla.png**: captura del gmsh, mostrando la malla generada
