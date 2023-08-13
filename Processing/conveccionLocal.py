#Matriz de rigidez local y vector de calor local por conveccion
#Toma como argumentos:
#X: matriz de coordenadas de los nodos
#MC3De: fila (e) de la matriz de conectividades 3D (tetrahedros) -> elemento (e)
#hc: coeficiente de conveccion
#T_aire: temperatura del aire ambiente
#plano: el plano del elemento tetragonal coincidente con la superficie de integracion
#nGauss: numero de puntos de Gauss
#Devuelve la matriz de rigidez local debida a la conveccion y 
#el vector de calor local debido a la conveccion
def conveccion(X,MC3De,hc,T_aire,plano,nGauss):
    #Cantidad de nodos x elemento tetragonal
    nodosXelemento3D = 4
    #Coordenadas gloables de los nodos del elemento e
    Xe = np.zeros((nodosXelemento3D,4))
    for i in range(4):
        Xe[i] = X[int(MC3De[i]-1)]
    #Xe = [[nodo1(e), x1(e), y1(e), z1(e)],
    #      [nodo2(e), x2(e), y2(e), z2(e)],
    #      [nodo3(e), x3(e), y3(e), z3(e)],
    #      [nodo4(e), x4(e), y4(e), z4(e)]]
    #Se obtienen los pesos y puntos de Gauss
    r,w = intregralGauss(nGauss)
    #Se inicializa la matriz de rigidez local
    Kce = np.zeros((nodosXelemento3D,nodosXelemento3D))
    #Se inicializa el vector de calor local por conveccion
    Qce = np.zeros((nodosXelemento3D,1))
    #Se recorren los puntos de Gauss
    for a in range(nGauss):
        for b in range(nGauss):
            #Si la superficie de conveccion del tetraedro es el plano 234:
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
                Φ = np.array([[0,1-θ1-θ2,θ1,θ2]])
                #Se calcula la traspuesta
                ΦT = np.reshape(Φ,(nodosXelemento3D,1))
                #Coordenadas de los nodos {2,3,4}
                x2,y2 = Xe[1][1], Xe[1][2]
                x3,y3 = Xe[2][1], Xe[2][2]
                x4,y4 = Xe[3][1], Xe[3][2]
                #Se obtiene la matriz jacobiana
                matrizJ = np.array([[x3-x2,y3-y2],
                                    [x4-x2,y4-y2]])
                #Se calcula el determinante
                J = abs(np.linalg.det(matrizJ))
                
            #Si la superficie de conveccion del tetraedro es el plano 134:
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
                Φ = np.array([funcion_Φ(0,ξ,τ)])
                #Se calcula la traspuesta
                ΦT = np.reshape(Φ,(nodosXelemento3D,1))
                #Se obtiene la matriz de las funciones de forma
                dΦ = funcion_dΦ(0,ξ,τ)
                #Se obtiene la matriz jacobiana
                matrizJ = funcion_J(X, MC3De, dΦ)
                #Al estar en el plano 134, se borra la fila 1
                matrizJ = np.delete(matrizJ,0,axis=0)
                #Al estar en el plano xy (z=cte), se borra la columna 3
                matrizJ = np.delete(matrizJ,2,axis=1)
                #Se calcula el jacobiano
                J = abs(np.linalg.det(matrizJ))

            #Si la superficie de conveccion del tetraedro es el plano 124:
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
                Φ = np.array([funcion_Φ(η,0,τ)])
                #Se calcula la traspuesta
                ΦT = np.reshape(Φ,(nodosXelemento3D,1))
                #Se obtiene la matriz de las funciones de forma
                dΦ = funcion_dΦ(η,0,τ)
                #Se obtiene la matriz jacobiana
                matrizJ = funcion_J(X, MC3De, dΦ)
                #Al estar en el plano 124, se borra fila 2
                matrizJ = np.delete(matrizJ,1,axis=0)
                #Al estar en el plano xy (z=cte), se borra la columna 3
                matrizJ = np.delete(matrizJ,2,axis=1)
                #Se calcula el jacobiano
                J = abs(np.linalg.det(matrizJ))
                
            #Si la superficie de conveccion del tetraedro es el plano 123:
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
                Φ = np.array([funcion_Φ(η,ξ,0)])
                #Se calcula la traspuesta
                ΦT = np.reshape(Φ,(nodosXelemento3D,1))
                #Se obtiene la matriz de las funciones de forma
                dΦ = funcion_dΦ(η,ξ,0)
                #Se obtiene la matriz jacobiana
                matrizJ = funcion_J(X, MC3De, dΦ)
                #Al estar en el plano 123, se borra la fila 3
                matrizJ = np.delete(matrizJ,2,axis=0)
                #Al estar en el plano xy (z=cte), se borra la columna 3
                matrizJ = np.delete(matrizJ,2,axis=1)
                #Se calcula el jacobiano
                J = abs(np.linalg.det(matrizJ))
            
            #Se calcula la matriz de rigidez local por conveccion
            Kce += w[a]*w[b]*hc*J*Jlm*Juv*np.matmul(ΦT,Φ)
            #Se calcula el vector de calor local por conveccion
            Qce += w[a]*w[b]*hc*T_aire*J*Jlm*Juv*ΦT
            
    return Kce, Qce
