#Matriz de masa local
#Toma como argumentos:
#X: matriz de coordenadas de los nodos
#MC3De: fila (e) de la matriz de conectividades 3D (hexaedros) -> elemento (e)
#α: difusividad termica del material del disco
#ρcp: densidad por el calor especifico del material del disco
#nGauss: numero de puntos de Gauss
def funcion_Mlocal(X,MC3De,ω,α,ρcp,nGauss):
    #Cantidad de nodos x elemento tetragonal
    nodosXelemento3D = 4
    #Se obtienen los pesos y puntos de Gauss
    r,w = intregralGauss(nGauss)
    #Se inicializan las matrices de masa locales
    MGe = np.zeros((nodosXelemento3D,nodosXelemento3D))
    MPe = np.zeros((nodosXelemento3D,nodosXelemento3D))
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
                #Se obtienen el vector de las funciones de forma
                Φ = np.array([funcion_Φ(η,ξ,τ)])
                #Se calcula la traspuesta
                ΦT = Φ.transpose()
                #Se obtiene la matriz gradiente de las funciones de forma
                dΦ = funcion_dΦ(η,ξ,τ)
                #Se obtiene la matriz jacobiana
                matrizJ = funcion_J(X,MC3De,dΦ)
                #Se calcula el jacobiano de la transformacion x,y,z -> η,ξ,τ
                J = abs(np.linalg.det(matrizJ))
                #Se calcula la matriz de masa local de Galerkin
                MGe += w[a]*w[b]*w[c]*ρcp*J*Jlmn*Juvw*np.matmul(ΦT,Φ)
                #Se obtiene el vector de pesos de Petrov
                W = np.array([funcion_W(η,ξ,τ, X, MC3De, ω, α)])
                #Se calcula la traspuesta
                WT = W.transpose()
                #Se calcula la matriz de masa local de Petrov
                MPe += w[a]*w[b]*w[c]*ρcp*J*Jlmn*Juvw*np.matmul(WT,Φ)
    #Matriz de masa local total
    Me = MGe + MPe
    return Me
