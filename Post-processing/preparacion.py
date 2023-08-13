#Se importan librerias
#numpy para operar con los arrays, cargar los resultados, etc...
import numpy as np
#matplotlib para graficar en 2D
import matplotlib.pyplot as plt
#pyvista para graficar en 3D (imagenes y videos)
import pyvista as pv
#curve_fit de scipy para trazar curvas que ajusten los datos
from scipy.optimize import curve_fit

#Informacion del mallado (PREPROCESSING)
with open('Malla5//disco.msh','r') as m:
    #Se saltean las primeras 4 lineas
    for i in range(4):
        m.readline()
    #Se obtiene la cantidad de Physical Groups
    nPhysicalGroups = int(m.readline())
    #Se crea un diccionario vacio de los Physical Groups
    physicalGroups = {}
    #Se recorren los Physical Groups
    for i in range(nPhysicalGroups):
        #Se lee y se separa cada linea
        pg = m.readline().split()
        #Se convierte el numero identificador del Physical Group (str) a int
        idPhysGroup = int(pg[1])
        #Se asocia cada numero identificador a su respectivo nombre
        physicalGroups[idPhysGroup] = pg[2].replace('"', '')
    #Se saltean 2 lineas
    m.readline()
    m.readline()
    #Numero de nodos
    nNodos = int(m.readline())
    #Se crea ahora una matriz de coordenadas globales de los nodos de la forma
    # [X] = [[1,x1,y1,z1],
    #        [2,x2,y2,z2],
    #        [3,x3,y3,z3],
    #        [    ...   ],
    #        [n,xn,yn,zn]]
    X = np.loadtxt(m,max_rows=nNodos)
    #Se saltean 2 lineas
    m.readline()
    m.readline()
    #Numero de elementos totales
    nElementos = int(m.readline())
    #Numero de elementos triangulares (sale de statistics en gmsh)
    nElementos2D = 1332 #triangulos (de 3 nodos)
    #Numero de elementos tetraedricos (sale de statistics en gmsh)
    nElementos3D = 2272 #tetraedros (de 4 nodos)
    #Se almacena la informacion de los elementos en un array (conectividad)
    MC2D = np.loadtxt(m,dtype=int,max_rows=nElementos2D)
    MC3D = np.loadtxt(m,dtype=int,max_rows=nElementos3D)
    #Estos arrays contienen la informacion siguiente:
    #Columna 0: numero de elemento
    #Columna 1: numero del tipo de elemento (2: triangulo de 3 nodos, 
    #4: tetraedro de 4 nodos)
    #Columna 2: numero de ctes (siempre son 2, no es importante)
    #Columna 3: numero de physical group
    #Columna 4: numero de la superficie/volumen a la cual pertenece el 
    #elemento (no es importante)
    #Columna 5+: numeros de los nodos que pertenecen al elemento

#Se crea una matriz que contenga unicamente los nodos de cada elemento 3D
#Es decir, se filtra la matriz MC3D, de manera que queden unicamente las 
#ultimas 4 columnas
MC3D = np.delete(MC3D,[0,1,2,3,4],axis=1)

#Velocidad considerada (depende del caso)
V = 250 #km/h 
#Se cargan los resultados obtenidos del processing
path = f'RESULTADOS//NO LINEAL//{V}kmh//resultados_{V}.txt'
T = np.loadtxt(path,delimiter=',')
#Temperatura maxima alcanzada
Tmax = np.amax(T)
print(f'Temperatura maxima: {Tmax}')
