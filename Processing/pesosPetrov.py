#Pesos de Petrov
#Toma como argumentos:
#η,ξ,τ: coordenadas convectivas locales
#X: matriz de coordenadas de los nodos
#MC3De: fila (e) de la matriz de conectividades (tetrahedros)
#ω: velocidad angular
#α: difusividad termica
def funcion_W(η,ξ,τ,X,MC3De,ω,α):
    if ω == 0:
        W = np.zeros(4)
    else:
        nodosXelemento3D = 4
        #Coordenadas gloables de los nodos del elemento e
        Xe = np.zeros((nodosXelemento3D,4))
        for i in range(nodosXelemento3D):
            Xe[i] = X[int(MC3De[i]-1)]
        #Xe = [[nodo1(e), x1(e), y1(e), z1(e)],
        #      [nodo2(e), x2(e), y2(e), z2(e)],
        #      [nodo3(e), x3(e), y3(e), z3(e)],
        #      [nodo4(e), x4(e), y4(e), z4(e)]]
        #Se obtienen el vector de las funciones de forma
        Φ = funcion_Φ(η,ξ,τ)
        #Se obtienen las derivadas de las funciones de forma
        dΦ = funcion_dΦ(η, ξ, τ)
        #Se calcula Φ.Xe en una variable auxiliar (aux)
        aux = np.matmul(Φ,Xe)
        #Coordenada x del elemento (e) interpolada
        x = aux[1]
        #Coordenada y del elemento (e) interpolada
        y = aux[2]
        #Vector velocidad de rotacion
        vd = np.array([-ω*y,ω*x,0])
        #Modulos de las componentes de la velocidad
        vx, vy = abs(vd[0]), abs(vd[1])
        #Velocidad absoluta
        Va = np.sqrt(vx**2 + vy**2)
        #Coordenadas xy de los nodos del elemento
        x1, y1 = Xe[0][1], Xe[0][2]
        x2, y2 = Xe[1][1], Xe[1][2]
        x3, y3 = Xe[2][1], Xe[2][2]
        x4, y4 = Xe[3][1], Xe[3][2]
        #Posibles longitudes caracteristicas del elemento (e)
        #Direccion x
        Lx12, Lx13, Lx14 = abs(x1 - x2), abs(x1 - x3), abs(x1 - x4)
        Lx23, Lx24 = abs(x2-x3), abs(x2-x4)
        Lx34 = abs(x3-x4)
        #Direccion y
        Ly12, Ly13, Ly14 = abs(y1 - y2), abs(y1 - y3), abs(y1 - y4)
        Ly23, Ly24 = abs(y2-y3), abs(y2-y4)
        Ly34 = abs(y3-y4)
        #Se toman las mayores longitudes como las caracteristicas del elemento
        Lx = max([Lx12,Lx13,Lx14,Lx23,Lx24,Lx34])
        Ly = max([Ly12,Ly13,Ly14,Ly23,Ly24,Ly34])
        #Numero de Peclet en cada direccion
        Pe_x = vx*Lx/(2*α)
        Pe_y = vy*Ly/(2*α)
        #Coeficiente auxiliar optimizado
        a_x = 1/np.tanh(abs(Pe_x)) - 1/abs(Pe_x)
        a_y = 1/np.tanh(abs(Pe_y)) - 1/abs(Pe_y)
        #Tiempo intriseco
        τi = a_x*Lx/(2*Va) + a_y*Ly/(2*Va)
        #Matriz jacobiana
        matrizJ = funcion_J(X,MC3De,dΦ)
        #Matriz B, de dimensiones (3x4)
        B = funcion_B(matrizJ, dΦ)
        #Se calcula el vector de pesos de Petrov, dimensiones (1x4)
        W = τi*np.matmul(vd,B)
    return W
