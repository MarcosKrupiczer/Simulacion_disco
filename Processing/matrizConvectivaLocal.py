#Matriz convectiva local
#Toma como argumentos:
#X: matriz de coordenadas de los nodos
#MC3De: fila (e) de la matriz de conectividades 3D (tetrahedros) -> elemento (e)
#α: difusividad termica
#ρcp: densidad por el calor especifico del disco
#ω: velocidad angular
#nGauss: numero de puntos de Gauss
def funcion_Nlocal(X,MC3De,α,ρcp,ω,nGauss):
    #Cantidad de nodos x elemento tetragonal
    nodosXelemento3D = 4
    if ω == 0:
        Ne = np.zeros((nodosXelemento3D,nodosXelemento3D))
    else:
        #Coordenadas globales de los nodos del elemento e
        Xe = np.zeros((4,4))
        for i in range(4):
            Xe[i] = X[int(MC3De[i]-1)]
        #Se obtienen los pesos y puntos de Gauss
        r,w = intregralGauss(nGauss)
        #Se inicializan las matrices convectivas locales
        NGe = np.zeros((nodosXelemento3D,nodosXelemento3D))
        NPe = np.zeros((nodosXelemento3D,nodosXelemento3D))
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
                    Φ = funcion_Φ(η,ξ,τ)
                    #Se calcula Φ.Xe en una variable auxiliar (aux)
                    aux = np.matmul(Φ,Xe)
                    #Coordenada x del elemento (e) interpolada
                    x = aux[1]
                    #Coordenada y del elemento (e) interpolada
                    y = aux[2]
                    #Vector velocidad de rotacion
                    vd = np.array([-ω*y,ω*x,0])
                    #Se calcula la traspuesta
                    ΦT = np.array([Φ]).transpose()
                    #Se obtiene la matriz gradiente de las funciones de forma
                    dΦ = funcion_dΦ(η,ξ,τ)
                    #Se obtiene la matriz jacobiana
                    matrizJ = funcion_J(X,MC3De,dΦ)
                    #Se calcula el jacobiano
                    J = abs(np.linalg.det(matrizJ))
                    #Se obtiene la matriz B
                    B = funcion_B(matrizJ,dΦ)
                    #Se calcula la matriz convectiva de Galerkin local
                    NGe += ρcp*w[a]*w[b]*w[c]*J*Jlmn*Juvw*np.matmul(ΦT,np.array([np.matmul(vd,B)]))
                    #Se obtiene el vector de pesos de Petrov
                    W = funcion_W(η,ξ,τ, X, MC3De, ω, α)
                    WT = np.array([W]).transpose()
                    #Se calcula la matriz convectiva de Petrov local
                    NPe += ρcp*w[a]*w[b]*w[c]*J*Jlmn*Juvw*np.matmul(WT,np.array([np.matmul(vd,B)]))
        #Matriz convectiva local total
        Ne = NGe + NPe
    return Ne
