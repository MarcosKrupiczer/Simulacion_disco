#Ensamble
#Toma como argumentos:
#X_orig: la matriz de coordenadas iniciales de los nodos
#X: la matriz de coordenadas de los nodos rotadas
#T: vector de temperaturas propuesto
#elem_neumann: lista de elementos 3D pertenecientes a la superficie Sq
#MC2D: matriz de conectividades de los elementos triangulares de 3 nodos
#nElementos2D: cantidad de elementos triangulares de 3 nodos
#MC3D: matriz de conectividades de los elementos tetragonales de 4 nodos
#nElementos3D: cantidad de elementos tetragonales de 4 nodos
#T_aire: temperatura del aire ambiente [K]
#CDA: coeficiente de Drag por Area del vehiculo [m^2]
#ω: velocidad angular
#γ: aceleracion angular
#m: masa del vehiculo
#nGauss: numero de puntos de Gauss para la integracion numerica
def ensamble(X_orig,X,T,elem_neumann,elem_conveccion,MC3D,nElementos3D,T_aire,CDA,ω,γ,V,m,nGauss):
    #Se inicializan las matrices y vectores globales
    M = np.zeros((nNodos,nNodos))
    Kk = np.zeros((nNodos,nNodos))
    Kc = np.zeros((nNodos,nNodos))
    N = np.zeros((nNodos,nNodos))
    Qk = np.zeros((nNodos,1))
    Qc = np.zeros((nNodos,1))
    #Nodos x elemento 3D
    nodosXelemento3D = 4
    #Se inicializa un vector de temperaturas de los elementos3D (tetragonales)
    Telem = np.zeros(nElementos3D)
    #Se recorren los elementos 3D
    for e in range(nElementos3D):
        #Se recorren los nodos del elemento (e)
        for j in range(nodosXelemento3D):
            #Se calcula el promedio de las temperaturas nodales y se la 
            #almacena en la posicion (e) del vector de temperaturas elementales
            Telem[e] += 1/nodosXelemento3D*T[int(MC3D[e][j]-1)][0]
        #Se obtiene la conductividad termica del elemento del disco
        #k = funcion_k_fundicion(Telem[e])
        k = funcion_k_fundicion(298)
        #Se obtiene el producto densidad calor especifico del elemento del disco
        #ρcp = funcion_ρcp_fundicion(Telem[e])
        ρcp = funcion_ρcp_fundicion(298)
        #Difusividad termica en el disco
        α = k/(ρcp)
        #Condicion de borde de conveccion
        if elem_conveccion[e]!=0:
            #Plano coincidente con la superficie Sc
            plano = elem_conveccion[e]
            if plano==123:
                #Coordenadas de los nodos del elemento
                x1,y1 = X[int(MC3D[e][0]-1)][1],X[int(MC3D[e][0]-1)][2] #1
                x2,y2 = X[int(MC3D[e][1]-1)][1],X[int(MC3D[e][1]-1)][2] #2
                x3,y3 = X[int(MC3D[e][2]-1)][1],X[int(MC3D[e][2]-1)][2] #3
            elif plano==124:
                #Coordenadas de los nodos del elemento
                x1,y1 = X[int(MC3D[e][0]-1)][1],X[int(MC3D[e][0]-1)][2] #1
                x2,y2 = X[int(MC3D[e][1]-1)][1],X[int(MC3D[e][1]-1)][2] #2
                x3,y3 = X[int(MC3D[e][3]-1)][1],X[int(MC3D[e][3]-1)][2] #4
            elif plano==134:
                #Coordenadas de los nodos del elemento
                x1,y1 = X[int(MC3D[e][0]-1)][1],X[int(MC3D[e][0]-1)][2] #1
                x2,y2 = X[int(MC3D[e][2]-1)][1],X[int(MC3D[e][2]-1)][2] #3
                x3,y3 = X[int(MC3D[e][3]-1)][1],X[int(MC3D[e][3]-1)][2] #4
            elif plano==234:
                #Coordenadas de los nodos del elemento
                x1,y1 = X[int(MC3D[e][1]-1)][1],X[int(MC3D[e][1]-1)][2] #2
                x2,y2 = X[int(MC3D[e][2]-1)][1],X[int(MC3D[e][2]-1)][2] #3
                x3,y3 = X[int(MC3D[e][3]-1)][1],X[int(MC3D[e][3]-1)][2] #4
            #Lados del triangulo
            a1 = np.sqrt((x2-x1)**2 + (y2-y1)**2)
            a2 = np.sqrt((x3-x2)**2 + (y3-y2)**2)
            a3 = np.sqrt((x3-x1)**2 + (y3-y1)**2)
            #Semi-perimetro
            s = (a1 + a2 + a3)/2
            #Area del triangulo
            Area = np.sqrt(s*(s-a1)*(s-a2)*(s-a3))
            #Longitud caracteristica
            Le = np.sqrt(Area)
            #Se obtiene el coeficiente de conveccion en la superficie del elemento
            hc = funcion_hc(V,Telem[e],T_aire,Le,plano)
            #Se obtiene la matriz de rigidez de conveccion local
            #y el vector de calor por conveccion local
            Kce, Qce = conveccion(X,MC3D[e],hc,T_aire,plano,nGauss)
        elif elem_conveccion[e]==0:
            Kce = np.zeros((nodosXelemento3D,nodosXelemento3D))
            Qce = np.zeros((nodosXelemento3D,1))
            
        #Condicion de borde de neumann
        if elem_neumann[e]!=0:
            plano = elem_neumann[e]
            Qke = funcion_Qlocal(X_orig,MC3D[e],plano,ω,γ,k,ρcp,CDA,m,nGauss)
        elif elem_neumann[e]==0:
            Qke = np.zeros((nodosXelemento3D,1))
            
        #Se obtiene la matriz de rigidez por conduccion local
        Kke = funcion_Klocal_conduccion(X,MC3D[e],k,nGauss) 
        #Se obtiene la matriz convectiva local
        Ne = funcion_Nlocal(X,MC3D[e],α,ρcp,ω,nGauss)
        #Se obtiene la matriz de masa local
        Me = funcion_Mlocal(X,MC3D[e],ω,α,ρcp,nGauss)
        for i in range(nodosXelemento3D):
            #Vector de calor por conduccion global
            Qk[MC3D[e][i]-1][0] = Qk[MC3D[e][i]-1][0] + Qke[i][0]
            #Vector de calor por conveccion global
            Qc[MC3D[e][i]-1][0] = Qc[MC3D[e][i]-1][0] + Qce[i][0]
            for j in range(nodosXelemento3D):
                #Matriz de masa global
                M[MC3D[e][i]-1][MC3D[e][j]-1] = M[MC3D[e][i]-1][MC3D[e][j]-1] + Me[i][j]
                #Matriz convectiva global
                N[MC3D[e][i]-1][MC3D[e][j]-1] = N[MC3D[e][i]-1][MC3D[e][j]-1] + Ne[i][j]
                #Matriz de rigidez por conduccion global
                Kk[MC3D[e][i]-1][MC3D[e][j]-1] = Kk[MC3D[e][i]-1][MC3D[e][j]-1] + Kke[i][j]
                #Matriz de rigidez por conveccion global
                Kc[MC3D[e][i]-1][MC3D[e][j]-1] = Kc[MC3D[e][i]-1][MC3D[e][j]-1] + Kce[i][j]
       
    #Matriz de rigidez total
    K = Kk + Kc
    #Vector de calor total
    Q = Qk + Qc
    return M,N,K,Q
