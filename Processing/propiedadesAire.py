#Propiedades termicas del aire en funcion de la temperatura
#Conductividad termica
def funcion_k_aire(T):
    return 5.5744e-5*T + 0.010618
#Viscosidad cinematica
def funcion_ν_aire(T):
    return 6.6508e-11*T**2 + 5.8552e-8*T -8.2663e-6
