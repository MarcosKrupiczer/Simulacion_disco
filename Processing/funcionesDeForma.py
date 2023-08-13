#Funciones de forma
#Toma como argumentos las coordenadas convectivas de los elementos tetragonales
def funcion_Φ(η,ξ,τ):
    #Funciones de forma para elementos tetragonales
    φ1 = 1-η-ξ-τ
    φ2 = η
    φ3 = ξ
    φ4 = τ
    #Vector de funciones de forma
    Φ = np.array([φ1,φ2,φ3,φ4])
    return Φ
