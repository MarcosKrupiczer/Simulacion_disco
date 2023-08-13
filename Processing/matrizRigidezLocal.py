#Matriz de rigidez local de conduccion
#Toma como argumentos:
#X: matriz de coordenadas de los nodos
#MC3De: fila (e) de la matriz de conectividades 3D (tetrahedros) -> elemento (e)
#k: conductividad termica del material del disco
#nGauss: numero de puntos de Gauss
def funcion_Klocal_conduccion(X,MC3De,k,nGauss):
    #Se obtienen los pesos y puntos de Gauss
    r,w = intregralGauss(nGauss)
    #Cantidad de nodos x elemento tetragonal
    nodosXelemento3D = 4
    #Se inicializa la matriz de rigidez local
    Kke = np.zeros((nodosXelemento3D,nodosXelemento3D)) 
    #Se recorren los puntos de Gauss
    for a in range(nGauss):
        for b in range(nGauss):
            for c in range(nGauss):
                #3er mapeo (transforma el 1-cubo en 2-cubo)
                l = (1+r[a])/2 # u = r[a]
                m = (1+r[b])/2 # v = r[b]
                n = (1+r[c])/2 # w = r[c]
                #Jacobiano de la transformacion l,m,n -> u,v,w
                Juvw = 1/8
                #2do mapeo (transforma el tetraedro en 1-cubo)
                η = l*m*n
                ξ = l*m*(1-n)
                τ = l*(1-m)
                #Jacobiano de la transformacion η,ξ,τ -> l,m,n
                Jlmn = abs(l**2*m)
                #Se obtiene la matriz de derivadas de las funciones de forma
                dΦ = funcion_dΦ(η,ξ,τ)
                #Se obtiene la matriz jacobiana
                matrizJ = funcion_J(X,MC3De,dΦ)
                #Se calcula el jacobiano
                J = abs(np.linalg.det(matrizJ))
                #Se obtiene la matriz B
                B = funcion_B(matrizJ,dΦ)
                #Se calcula la traspuesta de B
                BT = np.transpose(B)
                #Se calcula la matriz de rigidez local por conduccion
                Kke += w[a]*w[b]*w[c]*k*J*Jlmn*Juvw*np.matmul(BT,B)
    return Kke
