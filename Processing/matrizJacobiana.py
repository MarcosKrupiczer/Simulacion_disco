#Matriz jacobiana elemental de la transformacion de coordenadas cartesianas (globales) a las convectivas (locales)
#Toma como argumentos:
#X: matriz de coordenadas de los nodos
#MC3De: fila (e) de la matriz de conectividades 3D (tetraedros) -> elemento (e)
#dΦ: matriz de derivadas de las funciones de forma
def funcion_J(X,MC3De,dΦ):
    #Nodos x elemento tetragonal
    nodosXelemento3D = 4
    #Coordenadas globales de los nodos del elemento e
    Xe = np.zeros((nodosXelemento3D,4))
    for i in range(nodosXelemento3D):
        Xe[i] = X[int(MC3De[i]-1)]
    #Xe = [[1,x1,y1,z1],
    #      [2,x2,y2,z2],
    #      [3,x3,y3,z3],
    #      [4,x4,y4,z4]] del elemento (e)
    #Derivada de (x,y,z) respecto de (η,ξ,τ)
    #Inicializacion de las derivadas de x
    x_η, x_ξ, x_τ = 0, 0, 0
    #Inicializacion de las derivadas de y
    y_η, y_ξ, y_τ = 0, 0, 0
    #Inicializacion de las derivadas de z
    z_η, z_ξ, z_τ = 0, 0, 0
    #Sumatoria
    for i in range(nodosXelemento3D):
        #Derivadas de x
        x_η += dΦ[0][i]*Xe[i][1]
        x_ξ += dΦ[1][i]*Xe[i][1]
        x_τ += dΦ[2][i]*Xe[i][1]
        #Derivadas de y
        y_η += dΦ[0][i]*Xe[i][2]
        y_ξ += dΦ[1][i]*Xe[i][2]
        y_τ += dΦ[2][i]*Xe[i][2]
        #Derivadas de z
        z_η += dΦ[0][i]*Xe[i][3]
        z_ξ += dΦ[1][i]*Xe[i][3]
        z_τ += dΦ[2][i]*Xe[i][3]
    #Matriz jacobiana
    matrizJ = np.array([[x_η,y_η,z_η],
                        [x_ξ,y_ξ,z_ξ],
                        [x_τ,y_τ,z_τ]])
    return matrizJ
