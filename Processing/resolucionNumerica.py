#Numero de puntos de Gauss en cada direccion
n = 2
#Se busca resolver el sistema dinamico siguiente:
# [M]*{dT/dt} + ([N] + [K])*{T} = {Q}
#Se resuelve mediante el metodo de Crank-Nicholson (Diferencias centradas) iterando con el metodo de Picard
β = 0.5 #parametro que define diferencias centradas
#Tiempo inicial
t = 0
#Se supone la temperatura inicial uniforme en t=Δt para la 1era iteracion
T_anterior = T0*np.ones((nNodos,1)) #anterior se refiere al instante t
#En este caso, es el instante t=0
T = T_anterior #ningun subindice se refiere al instante t+Δt
#Esta temperatura es: T(t+Δt) en t=0, iteracion k=0
#Tolerancia porcentual (1%)
tol = 1 #%
#Se inicializa el vector de error porcentual
er = np.zeros(nNodos)
#Contador de interaciones para un mismo paso temporal
i = 0
#Contador del paso temporal
p = 1
#Paso temporal
Δt_min = 0.1
print(f'Paso temporal inicial: Δt = {Δt_min}[s]')
#Paso de tiempo maximo
Δt_max = 10 #s
#Tiempo adicional con el auto parado
δt = 300 #s
#Se inicializa una matriz de resultados
Resultados = np.zeros((int(1+(tf+δt-t0)/Δt_min),nNodos))
#La matriz de resultados sera de la forma:
#Resultados = [[T1(t0), T2(t0), T3(t0), ... , Tn(t0)],
#              [T1(t1), T2(t1), T3(t1), ... , Tn(t1)],
#              [ ...   , ...  ,  ...  , ... ,  ...  ],
#              [T1(tf), T2(tf), T3(tf), ... , Tn(tf)]]
#Es decir, Resultados[i][j] es la temperatura del nodo j en el tiempo ti
#Se coloca la temperatura inicial en la 1era fila de la matriz de resultados
Resultados[0] = T_anterior.flatten()

#Se inicializan las matrices de coordenadas nodales rotadas
Xrot_anterior = np.zeros((nNodos,4))
Xrot = np.zeros((nNodos,4))
#Se avanza en el tiempo
with open(f'resultados_{Vkmh}.txt','w') as res:
    for itera in range(nNodos-1):
        res.write(f'{Resultados[0][itera]},')
    res.write(f'{Resultados[0][-1]}')
    res.write('\n')
    while t<tf+δt:
        #Se comienza usando el paso temporal minimo
        Δt = Δt_min
        #Angulo de rotacion en tiempo t
        θ_anterior = ω0*t+γ*t**2/2
        #Matriz de rotacion en tiempo t
        Rθ_anterior = np.array([[np.cos(θ_anterior),-np.sin(θ_anterior),0],
                                [np.sin(θ_anterior),np.cos(θ_anterior),0],
                                [0,0,1]])
        #Se calculan las coordenadas de los nodos en el tiempo t
        for j in range(nNodos):
            xyz_rot_anterior = np.matmul(Rθ_anterior,np.reshape(X[j][1:4],(3,1))).flatten()
            Xrot_anterior[j] = [i+1,xyz_rot_anterior[0],xyz_rot_anterior[1],xyz_rot_anterior[2]]
        #Angulo de rotacion en tiempo t+Δt
        θ = ω0*(t+Δt)+γ*(t+Δt)**2/2
        #Matriz de rotacion en tiempo t+Δt
        Rθ = np.array([[np.cos(θ),-np.sin(θ),0],
                       [np.sin(θ),np.cos(θ),0],
                       [0,0,1]])
        #Se calculan las coordenadas de los nodos en el tiempo t+Δt
        for j in range(nNodos):
            xyz_rot = np.matmul(Rθ,np.reshape(X[j][1:4],(3,1))).flatten()
            Xrot[j] = [j+1,xyz_rot[0],xyz_rot[1],xyz_rot[2]]
            
        #Se calculan las velocidades lineal y angular en el tiempo t
        ω_anterior = ω0*(1-t/tf)
        V_anterior = ω_anterior*Rr
        #Se calculan las velocidades lineal y angular en el tiempo t+Δt
        ω = ω0*(1-(t+Δt)/tf)
        V = ω*Rr
        #Si la velocidad en t+Δt se vuelve negativa, el vehiculo debe estar detenido:
        if ω <= 0 and ω_anterior>0:
            #Se fija la velocidad en (t+Δt) =0
            V = 0
            ω = 0
            #Se obtienen las matrices y vectores en t
            M_anterior,N_anterior,K_anterior,Q_anterior = ensamble(X,X,T_anterior,elem_neumann,elem_conveccion,MC3D,nElementos3D,T_aire,CDA,ω_anterior,γ,V_anterior,m,n)
            #Se obtienen las matrices y vectores en t+Δt
            M,N,K,Q = ensamble(X,X,T,elem_neumann,elem_conveccion,MC3D,nElementos3D,T_aire,CDA,ω,γ,V,m,n)
        #Si la velocidad en t se vuelve negativa, el vehiculo esta a punto de detenerse:
        elif ω_anterior <= 0:
            #Se fija la velocidad en (t) =0
            V_anterior = 0
            ω_anterior = 0
            #Se fija la velocidad en (t+Δt) =0
            V = 0
            ω = 0
            #Se obtienen las matrices y vectores en t
            M_anterior,N_anterior,K_anterior,Q_anterior = ensamble(X,X,T_anterior,elem_neumann,elem_conveccion,MC3D,nElementos3D,T_aire,CDA,ω_anterior,γ,V_anterior,m,n)
            #Se obtienen las matrices y vectores en t+Δt
            M,N,K,Q = ensamble(X,X,T,elem_neumann,elem_conveccion,MC3D,nElementos3D,T_aire,CDA,ω,γ,V,m,n)
            #Se define el paso temporal variable
            Δt = Δt_max*(1-np.exp(-(t-tf)/tf))+ Δt_min
            print(f'Paso temporal: {Δt}[s]')
        else:
            #Se obtienen las matrices y vectores en t
            M_anterior,N_anterior,K_anterior,Q_anterior = ensamble(X,Xrot_anterior,T_anterior,elem_neumann,elem_conveccion,MC3D,nElementos3D,T_aire,CDA,ω_anterior,γ,V_anterior,m,n)
            #Se obtienen las matrices y vectores en t+Δt
            M,N,K,Q = ensamble(X,Xrot,T,elem_neumann,elem_conveccion,MC3D,nElementos3D,T_aire,CDA,ω,γ,V,m,n)

        #Se calcula una matriz auxiliar
        A = 1/Δt*((1-β)*M_anterior+β*M) + β*((1-β)*(N_anterior+K_anterior)+β*(N+K))
        #Se calcula un vector auxiliar
        b = (1-β)*Q_anterior + β*Q + (1/Δt*((1-β)*M_anterior+β*M)-(1-β)*((1-β)*(N_anterior+K_anterior)+β*(N+K))).dot(T_anterior)
        #Se calcula el nuevo vector de temperaturas en t+Δt (iteracion k+1)
        T_nueva = np.linalg.solve(A,b)
        print(f'Tmin = {min(T_nueva)} , Tmax = {max(T_nueva)}')
        #Chequeo de estabilidad (radio espectral <=1)
        #Matrices auxiliares
        C = 1/Δt*((1-β)*M_anterior+β*M)-(1-β)*((1-β)*(N_anterior+K_anterior)+β*(N+K))
        D = np.matmul(np.linalg.inv(A),C)
        #Radio espectral
        radio_espectral = abs(max(np.linalg.eigvals(D)))
        if radio_espectral<1.2:
            print(f'Radio espectral: {radio_espectral} ≈ 1 => Estabilidad asegurada')
        else:
            print(f'Radio espectral: {radio_espectral} > 1 => Estabilidad no asegurada')
        #Se compara la nueva temperatura (k+1) con la anterior (k)
        for j in range(nNodos):
            er[j] = 100*(abs(T_nueva[j][0]-T[j][0]))/T_nueva[j][0]
        #Si el error maximo es menor o igual a la tolerancia:
        if max(er)<=tol:
            #Se guarda el vector de temperaturas T(t+Δt) en la matriz de resultados
            Resultados[p] = T_nueva.flatten()
            print(f'Se ha guardado el vector T({t+Δt}[s]) en {time()-tiempo_inicial}[s] de tiempo computacional acumulado')
            print(f'Maximo error relativo: {max(er)} % < {tol} %')
            print()
            #Se actualiza el valor de los vectores de temperaturas: T(t) y 
            #T(t+Δt)(k=0) por el nuevo: T_nueva
            T_anterior = T_nueva
            T = T_nueva
            #Se incrementa un paso temporal
            t += Δt
            #Se guardan los resultados en un .txt en formato CSV (separado por ,)
            for i in range(nNodos-1):
                res.write(f'{Resultados[p][i]},')
            res.write(f'{Resultados[p][-1]}')
            res.write('\n')
            p += 1
            #Se vuelve a inicializar el contador de iteraciones
            i = 0
            #Salida de emergencia del bucle
            if t>tf+δt:
                break
        #En caso contrario,
        else:
            print(f't={t+Δt} s, iteracion {i} completada en {time()-tiempo_inicial}[s] de tiempo computacional acumulado')
            print(f'Maximo error relativo: {max(er)} % > {tol} %')
            print()
            #Se actualiza el valor del vector de temperaturas con las nueva para seguir iterando en el mismo paso temporal
            T = T_nueva
            #Se suma 1 al contador de iteraciones
            i += 1
