#Vector de calor local debido a la friccion entre pastilla y disco
#Toma como argumentos:
#X: matriz de coordenadas de los nodos de la malla inicial
#MC3De: fila (e) de la matriz de conectividades 3D (hexaedros) -> elemento (e)
#plano: plano sobre el cual se integra (123, 124, 134 o 234)
#ω: velocidad angular
#γ: aceleracion angular
#ρcp: densidad por el calor especifico del disco
#CDA: coeficiente de drag por el area de referencia
#m: masa del vehiculo
#nGauss: numero de puntos de Gauss
def funcion_Qlocal(X,MC3De,plano,ω,γ,k,ρcp,CDA,m,nGauss):
    #Cantidad de nodos x elemento tetragonal
    nodosXelemento3D = 4
    if ω == 0:
        Qqe = np.zeros((nodosXelemento3D,1))
    else:
        #Radio de la rueda
        Rr = 0.3 #m
        #Area de contacto pastilla-disco
        Ac = 0.00587958 #m^2
        #Coordenadas globales de los nodos del elemento e
        Xe = np.zeros((nodosXelemento3D,4))
        for i in range(4):
            Xe[i] = X[int(MC3De[i]-1)]
        #Xe = [[nodo1(e), x1(e), y1(e), z1(e)],
        #      [nodo2(e), x2(e), y2(e), z2(e)],
        #      [nodo3(e), x3(e), y3(e), z3(e)],
        #      [nodo4(e), x4(e), y4(e), z4(e)]]
        #Se obtienen los pesos y puntos de Gauss
        r,w = intregralGauss(nGauss)
        #Se inicializa el vector de calor local por conduccion
        Qke = np.zeros((nodosXelemento3D,1))
        #Densidad del aire
        ρa = 1.2 #kg/m^3
        #Flujo de calor total
        q = -(m*Rr**2*ω*γ+0.5*ρa*CDA*Rr**3*ω**3)/(8*Ac)
        #Conductividad termica del la pastilla
        kp = 2.5 #W/mK
        #Densidad de la pastilla
        ρp = 1900 #kg/m**3
        #Calor especifico de la pastilla
        cpp = 950 #J/kgK
        #Relacion disco/pastilla
        κ = np.sqrt(k*ρcp)/(np.sqrt(k*ρcp)+np.sqrt(kp*ρp*cpp))
        #Flujo de calor absorbido por el disco
        qd = κ*q
        #Se recorren los puntos de Gauss
        for a in range(nGauss):
            for b in range(nGauss):
                #Si la superficie de neumann del tetraedro es el plano 234:
                if plano==234:
                    #Transformacion de 1-cuadrado a 2-cuadrado
                    l = (1+r[a])/2 # u = r[a]
                    m = (1+r[b])/2 # v = r[b]
                    #Jacobiano
                    Juv = 1/4
                    #Transformacion de triangulo a 1-cuadrado
                    θ1 = l*m
                    θ2 = l*(1-m)
                    #Jacobiano
                    Jlm = abs(l)
                    #Se obtienen el vector de las funciones de forma
                    Φ = np.array([0,1-θ1-θ2,θ1,θ2])
                    #Se calcula la traspuesta
                    ΦT = np.reshape(Φ,(nodosXelemento3D,1))
                    #Coordenadas de los nodos {2,3,4}
                    x2,y2 = Xe[1][1], Xe[1][2]
                    x3,y3 = Xe[2][1], Xe[2][2]
                    x4,y4 = Xe[3][1], Xe[3][2]
                    #Se obtiene la matriz jacobiana
                    matrizJ = np.array([[x3-x2,y3-y2],
                                        [x4-x2,y4-y2]])
                    #Se calcula el jacobiano
                    J = abs(np.linalg.det(matrizJ))
                                            
                #Si la superficie de neumann del tetraedro es el plano 134:
                elif plano==134:
                    #Transformacion de 1-cuadrado a 2-cuadrado
                    l = (1+r[a])/2 # u = r[a]
                    m = (1+r[b])/2 # v = r[b]
                    #Jacobiano
                    Juv = 1/4
                    #Transformacion de triangulo a 1-cuadrado
                    ξ = l*m
                    τ = l*(1-m)
                    #Jacobiano
                    Jlm = abs(l)
                    #Se obtienen el vector de las funciones de forma
                    Φ = funcion_Φ(0,ξ,τ)
                    #Se calcula la traspuesta
                    ΦT = np.reshape(Φ,(nodosXelemento3D,1))
                    #Se obtiene la matriz de las funciones de forma
                    dΦ = funcion_dΦ(0,ξ,τ)
                    #Se obtiene la matriz jacobiana
                    matrizJ = funcion_J(X, MC3De, dΦ)
                    #Se elimina la 1era fila (plano 134: η=cte)
                    matrizJ = np.delete(matrizJ,0,axis=0)
                    #Se elimina la 3era columna (z=cte)
                    matrizJ = np.delete(matrizJ,2,axis=1)
                    #Se calcula el jacobiano
                    J = abs(np.linalg.det(matrizJ))
                    
                #Si la superficie de neumann del tetraedro es el plano 124:
                elif plano==124:
                    #Transformacion de 1-cuadrado a 2-cuadrado
                    l = (1+r[a])/2 # u = r[a]
                    m = (1+r[b])/2 # v = r[b]
                    #Jacobiano
                    Juv = 1/4
                    #Transformacion de triangulo a 1-cuadrado
                    η = l*m
                    τ = l*(1-m)
                    #Jacobiano
                    Jlm = abs(l)
                    #Se obtienen el vector de las funciones de forma
                    Φ = funcion_Φ(η,0,τ)
                    #Se calcula la traspuesta
                    ΦT = np.reshape(Φ,(nodosXelemento3D,1))
                    #Se obtiene la matriz de las funciones de forma
                    dΦ = funcion_dΦ(η,0,τ)
                    #Se obtiene la matriz jacobiana
                    #Se obtiene la matriz jacobiana
                    matrizJ = funcion_J(X, MC3De, dΦ)
                    #Se elimina la 2da fila (plano 124: ξ=cte)
                    matrizJ = np.delete(matrizJ,1,axis=0)
                    #Se elimina la 3era columna (z=cte)
                    matrizJ = np.delete(matrizJ,2,axis=1)
                    #Se calcula el jacobiano
                    J = abs(np.linalg.det(matrizJ))

                #Si la superficie de neumann del tetraedro es el plano 123:
                elif plano==123:
                    #Transformacion de 1-cuadrado a 2-cuadrado
                    l = (1+r[a])/2 # u = r[a]
                    m = (1+r[b])/2 # v = r[b]
                    #Jacobiano
                    Juv = 1/4
                    #Transformacion de triangulo a 1-cuadrado
                    η = l*m
                    ξ = l*(1-m)
                    #Jacobiano
                    Jlm = abs(l)
                    #Se obtienen el vector de las funciones de forma
                    Φ = funcion_Φ(η,ξ,0)
                    #Se calcula la traspuesta
                    ΦT = np.reshape(Φ,(nodosXelemento3D,1))
                    #Se obtiene la matriz de las funciones de forma
                    dΦ = funcion_dΦ(η,ξ,0)
                    #Se obtiene la matriz jacobiana
                    matrizJ = funcion_J(X, MC3De, dΦ)
                    #Se elimina la 3era fila (plano 123: τ=cte)
                    matrizJ = np.delete(matrizJ,2,axis=0)
                    #Se elimina la 3era columna (z=cte)
                    matrizJ = np.delete(matrizJ,2,axis=1)
                    #Se calcula el jacobiano
                    J = abs(np.linalg.det(matrizJ))
                    
                #Se calcula el vector de calor
                Qqe += w[a]*w[b]*qd*J*Jlm*Juv*ΦT
                
    return Qqe
