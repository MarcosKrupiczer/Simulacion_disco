#Derivadas de las funciones de forma
#Toma como argumentos las coordenadas convectivas de los elementos tetragonales
def funcion_dΦ(η,ξ,τ):
    #Derivadas para los elementos tetragonales de 4 nodos
    #φ1
    φ1_η = -1
    φ1_ξ = -1
    φ1_τ = -1
    #φ2
    φ2_η = 1
    φ2_ξ = 0
    φ2_τ = 0
    #φ3
    φ3_η = 0
    φ3_ξ = 1
    φ3_τ = 0
    #φ4
    φ4_η = 0
    φ4_ξ = 0
    φ4_τ = 1
    #Matriz gradiente de las funciones de forma
    dΦ = np.array([[φ1_η,φ2_η,φ3_η,φ4_η],
                       [φ1_ξ,φ2_ξ,φ3_ξ,φ4_ξ],
                       [φ1_τ,φ2_τ,φ3_τ,φ4_τ]])
    return dΦ
