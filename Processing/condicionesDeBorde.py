def CB_neumann(nElementos2D,MC2D,nElementos3D,MC3D,X,physicalGroups):
    CB = np.zeros(nElementos3D)
    #Se recorren los elementos 2D
    for i in range(nElementos2D):
        #Si el elemento 2D esta sobre la superficie neumann:
        if physicalGroups[MC2D[i][3]]=='neumann':
            #Se recorren los elementos 3D
            for e in range(nElementos3D):
                #Coordenadas z de los nodos del elemento e
                z1,z2,z3,z4 = X[int(MC3D[e][0]-1)][3],X[int(MC3D[e][1]-1)][3],X[int(MC3D[e][2]-1)][3],X[int(MC3D[e][3]-1)][3]
                #Si los nodos 2,3,4 del tetraedro coinciden con los nodos del triangulo, y las coordenadas z son las mismas para esos nodos:
                if len(intersection(MC3D[e][[1,2,3]], MC2D[i][[5,6,7]]))==3 and z2==z3==z4:
                        #El plano 234 coincide con la superficie de neumann
                        CB[e] = 234 #(τ = 1-η-ξ)
                #Si los nodos 1,3,4 del tetraedro coinciden con los nodos del triangulo, y las coordenadas z son las mismas para esos nodos:
                if len(intersection(MC3D[e][[0,2,3]], MC2D[i][[5,6,7]]))==3 and z1==z3==z4:
                        #El plano 234 coincide con la superficie de neumann
                        CB[e] = 134 #(τ = 1-η-ξ)
                #Si los nodos 1,2,4 del tetraedro coinciden con los nodos del triangulo, y las coordenadas z son las mismas para esos nodos:
                if len(intersection(MC3D[e][[0,1,3]], MC2D[i][[5,6,7]]))==3 and z1==z2==z4:
                        #El plano 234 coincide con la superficie de neumann
                        CB[e] = 124 #(τ = 1-η-ξ)
                #Si los nodos 1,2,3 del tetraedro coinciden con los nodos del triangulo, y las coordenadas z son las mismas para esos nodos:
                if len(intersection(MC3D[e][[0,1,2]], MC2D[i][[5,6,7]]))==3 and z1==z2==z3:
                        #El plano 234 coincide con la superficie de neumann
                        CB[e] = 123 #(τ = 1-η-ξ)
    return CB

def CB_conveccion(nElementos2D,MC2D,nElementos3D,MC3D,X,physicalGroups):
    CB = np.zeros(nElementos3D)
    #Se recorren los elementos 2D
    for i in range(nElementos2D):
        #Si el elemento 2D esta sobre la superficie neumann:
        if physicalGroups[MC2D[i][3]]=='conveccion':
            #Se recorren los elementos 3D
            for e in range(nElementos3D):
                #Coordenadas z de los nodos del elemento e
                z1,z2,z3,z4 = X[int(MC3D[e][0]-1)][3],X[int(MC3D[e][1]-1)][3],X[int(MC3D[e][2]-1)][3],X[int(MC3D[e][3]-1)][3]
                #Si los nodos 2,3,4 del tetraedro coinciden con los nodos del triangulo, y las coordenadas z son las mismas para esos nodos:
                if len(intersection(MC3D[e][[1,2,3]], MC2D[i][[5,6,7]]))==3 and z2==z3==z4:
                        #El plano 234 coincide con la superficie de neumann
                        CB[e] = 234 #(τ = 1-η-ξ)
                #Si los nodos 1,3,4 del tetraedro coinciden con los nodos del triangulo, y las coordenadas z son las mismas para esos nodos:
                if len(intersection(MC3D[e][[0,2,3]], MC2D[i][[5,6,7]]))==3 and z1==z3==z4:
                        #El plano 234 coincide con la superficie de neumann
                        CB[e] = 134 #(τ = 1-η-ξ)
                #Si los nodos 1,2,4 del tetraedro coinciden con los nodos del triangulo, y las coordenadas z son las mismas para esos nodos:
                if len(intersection(MC3D[e][[0,1,3]], MC2D[i][[5,6,7]]))==3 and z1==z2==z4:
                        #El plano 234 coincide con la superficie de neumann
                        CB[e] = 124 #(τ = 1-η-ξ)
                #Si los nodos 1,2,3 del tetraedro coinciden con los nodos del triangulo, y las coordenadas z son las mismas para esos nodos:
                if len(intersection(MC3D[e][[0,1,2]], MC2D[i][[5,6,7]]))==3 and z1==z2==z3:
                        #El plano 234 coincide con la superficie de neumann
                        CB[e] = 123 #(τ = 1-η-ξ)
    return CB

#Se obtienen los elementos sobre la superficie de Neumann (Sq)
elem_neumann = CB_neumann(nElementos2D,MC2D,nElementos3D,MC3D,X,physicalGroups)
#Se inicializa un contador
cont = 0
#Se recorren los elementos
for ite in range(len(elem_neumann)):
    #Si el numero de Neumann de cada elemento es distinto de 0
    if elem_neumann[ite]!=0:
        #Se suma 1 al contador
        cont+=1
#Se muestra un mensaje para avisar que se determinaron los elementos en la superficie Sq (y cuantos elementos son)
print(f'Se determinaron {cont} elementos en la superficie de neumann')
#Se obtienen los elementos sobre la superficie de conveccion (Sc)
elem_conveccion = CB_conveccion(nElementos2D,MC2D,nElementos3D,MC3D,X,physicalGroups)
#Se muestra un mensaje para avisar que se determinaron los elementos en la superficie Sc (y cuantos elementos son)
print('Se determinaron los elementos en la superficie de conveccion')
