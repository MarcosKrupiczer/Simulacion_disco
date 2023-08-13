# Simulación de un disco de frenos
Se simula por elementos finitos, un disco de frenos en distintas condiciones de procesos de frenado. Se plantea el problema como uno tridimensional, transitorio, no lineal, con una malla no estructurada de elementos tetragonales, y con una formulación Euleriana, es decir, se considera la velocidad de las partículas del disco en la ecuación diferencial.

La ecuación diferencial que gobierna el problema es:
$$^t\rho \ ^tc_p\frac{\partial ^tT}{\partial t}+\ ^t\rho \ ^tc_p \ ^t\underline{\text{v}_d}\cdot \ ^t\underline{\nabla} \ ^tT = \ ^tk \ ^t\nabla^2 \ ^tT$$

La velocidad total de cada particula del disco es igual a la suma de su velocidad de rotación ($^t\underline{\text{v}_d}$) y la velocidad de traslación del vehículo ($^t\underline{\text{v}_t}$).
$$^t\underline{\text{v}} \ = \ ^t\underline{\text{v}_d} \ + \ ^t\underline{\text{v}_t}$$
$$^t\underline{\text{v}_d} = -\ ^t\omega \ ^ty \ \underline{e_x} + \ ^t\omega \ ^tx \ \underline{e_y}$$
$$^t\underline{\text{v}_t} = -\ ^tV \ \underline{e_x}$$
Por motivos de estabilidad numérica, se considera únicamente la velocidad de rotación de las partículas en la ecuación diferencial.
