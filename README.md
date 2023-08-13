# Simulación de un disco de frenos
Se simula por elementos finitos, un disco de frenos en distintas condiciones de procesos de frenado. Se plantea el problema como uno tridimensional, transitorio, no lineal, con una malla no estructurada de elementos tetragonales, y con una formulación Euleriana, es decir, se considera la velocidad de las partículas del disco en la ecuación diferencial.

La ecuación diferencial que gobierna el problema es:

$^t\rho\:^tc_p\frac{\partial\,^tT}{\partial t}+\,^t\rho\,^tc_p\,^t\underline{\text{v}}\cdot\,^t\underline{\nabla}\,^tT = \,^tk\,^t\nabla^2\,^tT$

