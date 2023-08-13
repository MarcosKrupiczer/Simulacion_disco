#Datos y condiciones iniciales
#Radio de la rueda
Rr = 0.3 #m
#Tiempo inicial
t0 = 0
#Tiempo final
tf = 5 #s
#Velocidad inicial del vehiculo
Vkmh = 250 #km/h
#Se pasan las unidades a m/s
V0 = Vkmh*5/18
#Aceleracion (supuesta constante)
ac = -V0/tf
#Velocidad angular inicial
ω0 = V0/Rr #rad/s
#Velocidad angular final
ωf = 0
#Aceleracion angular (supuesta constante)
γ = (ωf-ω0)/(tf-t0)
#La velocidad angular en funcion del tiempo es:
# ω(t) = ω0 + γ*t
#Masa del auto
m = 1200 #kg
#Coeficiente de Drag por area de referencia
CDA = 0.6 #m^2
#Temperatura del aire ambiente
T_aire = 298 #K (25 grados celsius)
#Temperatura inicial del disco
T0 = 298 #K (25 grados celsius)
