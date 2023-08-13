#Integracion por Gauss-Legendre
#Toma como argumento el numero de puntos de Gauss (nGauss)
def intregralGauss(nGauss):
    #Iniciamos los vectores de pesos y posiciones de Gauss en cero
    w = np.zeros(int(nGauss)) #pesos
    r = np.zeros(int(nGauss)) #posiciones
    #Introducimos los valores de la tabla para cada n
    if nGauss==1:
      w[0] = 2
      r[0] = 0
    elif nGauss==2:
      r[0] = np.sqrt(1/3)
      r[1] = -np.sqrt(1/3)
      w[0] = 1
      w[1] = 1
    elif nGauss==3:
      r[0] = 0
      r[1] = np.sqrt(3/5)
      r[2] = -np.sqrt(3/5)
      w[0] = 8/9
      w[1] = 5/9
      w[2] = 5/9
    elif nGauss==4:
      r[0] = np.sqrt((3-2*np.sqrt(6/5))/7)
      r[1] = -np.sqrt((3-2*np.sqrt(6/5))/7)
      r[2] = np.sqrt((3+2*np.sqrt(6/5))/7)
      r[3] = -np.sqrt((3+2*np.sqrt(6/5))/7)
      w[0] = (18+np.sqrt(30))/36
      w[1] = (18+np.sqrt(30))/36
      w[2] = (18-np.sqrt(30))/36
      w[3] = (18-np.sqrt(30))/36
    return r,w
