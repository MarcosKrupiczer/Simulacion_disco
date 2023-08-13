#Coeficiente de conveccion
#Se calcula el coeficiente de conveccion hc local para cada elemento
#utilizando la correlacion de flujo forzado externo sobre placa plana
#Toma como argumentos:
#V: velocidad de traslacion del vehiculo [m/s]
#Te: temperatura del elemento (e) [K]
#T_aire: temperatura del aire ambiente [K]
#Le: longitud caracteristica del elemento (e) [m]
def funcion_hc(V,Te,T_aire,Le):
    if V==0:
        hc = 0
    else:
        #Temperatura de referencia
        TR = (Te+T_aire)/2
        #T es la temperatura del elemento considerado
        #Conductividad termica del aire
        ka = funcion_k_aire(TR)
        #Numero de Prandlt del aire
        Pr = 0.69
        #Viscosidad cinematica del aire 
        νa = funcion_ν_aire(TR)
        #Numero de Reynolds
        Re = V*Le/νa
        #Numero de Nusselt
        #Se supone flujo forzado externo a lo largo de placa plana
        #Caso laminar:
        if Re<5e5:
            Nu = 0.664*Re**(1/2)*Pr**(1/3)
        #Caso turbulento:
        else:
            Nu=0.664*Re**(1/2)*Pr**(1/3)+0.036*Re**0.8*Pr**0.43*(1-(5e5/Re)**0.8)
        #Coeficiente de conveccion
        hc = ka*Nu/Le
    return hc
