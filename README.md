# Simulación de un disco de frenos
Se simula por elementos finitos, un disco de frenos en distintas condiciones de procesos de frenado. Se plantea el problema como uno tridimensional, transitorio, no lineal, con una malla no estructurada de elementos tetragonales, y con una formulación Euleriana, es decir, se considera la velocidad de las partículas del disco en la ecuación diferencial.

La ecuación diferencial que gobierna el problema es:
$$^t\rho \ ^tc_p\frac{\partial ^tT}{\partial t}+\ ^t\rho \ ^tc_p \ ^t\underline{\text{v}_d}\cdot \ ^t\underline{\nabla} \ ^tT = \ ^tk \ ^t\nabla^2 \ ^tT$$

La velocidad total de cada particula del disco es igual a la suma de su velocidad de rotación ($^t\underline{\text{v}_d}$) y la velocidad de traslación del vehículo ($^t\underline{\text{v}_t}$).
$$^t\underline{\text{v}} \ = \ ^t\underline{\text{v}_d} \ + \ ^t\underline{\text{v}_t}$$
$$^t\underline{\text{v}_d} = -\ ^t\omega \ ^ty \ \underline{e_x} + \ ^t\omega \ ^tx \ \underline{e_y}$$
$$^t\underline{\text{v}_t} = -\ ^tV \ \underline{e_x}$$
Por motivos de estabilidad numérica, se considera únicamente la velocidad de rotación de las partículas en la ecuación diferencial. La componente de traslación se toma en cuenta agregando una condición de borde de convección:
$$q\_{\text{conv}}=-\ ^tk \ ^t\underline{\nabla} \ ^tT \cdot \underline{n\_c} = \ ^th_c\left(^tT-T\_{\infty}\right) \quad\quad ^t\underline{\text{x}} \ \in \ S\_c$$
Siendo $S_c$ la superficie del disco expuesta al aire exterior, $\underline{n\_c}$ su normal, y $T\_\infty$ la temperatura de referencia de del aire. El coeficiente de convección se obtiene a partir de la correlación de flujo forzado sobre una placa plana, utilizando únicamente la velocidad de traslación del vehículo. 

Se tiene también una condición de borde del tipo Neumann, que representa la generación de calor por fricción en la superficie de contacto entre la pastilla y el disco de frenos.
$$q=-\ ^tk \ ^t\underline{\nabla} \ ^tT \cdot \underline{n\_q}= \kappa \ \frac{m\frac{^tV^2}{t\_f} - \frac{1}{2}\rho\_\infty \ C\_D \ A\_R \ ^tV^3}{8 \ A\_f}\quad\quad ^t\underline{\text{x}} \ \in \ S\_q$$
Siendo:
- $m$ la masa del vehículo
- $^tV$ la velocidad del vehículo
- $t_f$ el tiempo de frenada
- $\rho\_\infty$ la densidad de referencia del aire
- $C\_D \ A\_R$ el coeficiente de Drag por el área de referencia
- $A\_f$ el área de contacto entre pastilla y disco de frenos (área de la superficie $S\_q$ con normal $\underline{n\_q}$)
- $\kappa$ un coeficiente que determina qué porción de calor es absorbida por el disco: $\kappa=\frac{\sqrt{k \ c\_p \ \rho}}{\sqrt{k \ c\_p \ \rho} + \sqrt{k\_p \ c\_{p_p} \ \rho\_p}}
Donde las propiedades con subíndice $p$ son las de la pastilla de frenos.
