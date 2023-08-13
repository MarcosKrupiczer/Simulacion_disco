#Matriz B (gradiente de las funciones de forma)
#Toma como argumentos:
#matrizJ: matriz jacobiana
#dΦ: matriz de derivadas de las funciones de forma
def funcion_B(matrizJ,dΦ):
    #Inversa de la matriz jacobiana
    matrizJ_inv = np.linalg.inv(matrizJ)
    #Matriz B
    B = np.matmul(matrizJ_inv,dΦ)
    return B
