#Propiedades termicas del material del disco (fundicion de hierro) en funcion de la temperatura
#Conductividad termica
def funcion_k_fundicion(T):
    return -8.22099060e-05*(T - 4.90413792e+02)**2 + 4.07923450e+01
#Densidad por el calor especifico
def funcion_ρcp_fundicion(T):
    return 2.06765696e+03*T + 2.67410206e+06
