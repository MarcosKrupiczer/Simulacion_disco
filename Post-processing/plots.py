#GRAFICOS de T(r')
#Dimensiones
R1 = 35e-3 #m
R2 = 85e-3 #m
R3 = 150e-3 #m
#Radio total del disco + tramo entre planos
RT = 190e-3 #m
e1 = 15e-3 #m
e = 25e-3 #m
#Coordenada pseudo-radial continua
pseudo_r_cont = np.linspace(R1/RT,RT/RT,300)
#Coordenada pseudo-radial discreta
pseudo_r = []
#Se crea una figura
plt.figure(figsize=(6.5,5),dpi=120)

#Se recorren los nodos
for i in range(nNodos):
    #Se obtienen las coordenadas cartesianas
    x, y, z = X[i][1], X[i][2], X[i][3]
    #Se obtiene el numero del nodo
    nodo = X[i][0]
    #Se calcula la coordenada radial
    r = np.sqrt(x**2 + y**2)
    #Se calcula la coordenada pseudo-radial
    if r>=80e-3:
        #Se agrega el nodo y la coordenada pseudo-radial adimensionalizada
        pseudo_r.append([nodo,(r+e-z)/RT])
    else:
        #Se agrega el nodo y la coordenada pseudo-radial adimensionalizada
        pseudo_r.append([nodo,r/RT])

pseudo_r = np.array(pseudo_r)

#Se define un modelo de interpolacion de orden cinco
def model(x,a,b,c,d,e,f,g,h):
    return a*x**7 + b*x**6 + c*x**5 + d*x**4 + e*x**3 + f*x**2 + g*x + h

#Tiempo t = 0
t = 0
#Se obtiene la interpolacion
popt0, _ = curve_fit(model,pseudo_r[:,1],T[int(10*t)])
#Coeficientes
a,b,c,d,e,f,g,h = popt0
interpol0 = model(pseudo_r_cont,a,b,c,d,e,f,g,h)
plt.plot(pseudo_r_cont,interpol0,color='tab:blue',label=r"$\left.T(r')\right.|_{t=0}$")

plt.scatter(pseudo_r[:,1],T[int(10*t)],s=10,color='tab:blue')



#Tiempo t = 2.5 s
t = 2.5
#Se obtiene la interpolacion
popt1, _ = curve_fit(model,pseudo_r[:,1],T[int(10*t)])
#Coeficientes
a,b,c,d,e,f,g,h = popt1
interpol1 = model(pseudo_r_cont,a,b,c,d,e,f,g,h)
plt.plot(pseudo_r_cont,interpol1,color='tab:orange',label=r"$\left.T(r')\right.|_{t=0,5\,t_f}$")

plt.scatter(pseudo_r[:,1],T[int(10*t)],s=10,color='tab:orange')


#Tiempo t = 5 s
t = 5
#Se obtiene la interpolacion
popt2, _ = curve_fit(model,pseudo_r[:,1],T[int(10*t)])
#Coeficientes
a,b,c,d,e,f,g,h = popt2
interpol2 = model(pseudo_r_cont,a,b,c,d,e,f,g,h)
plt.plot(pseudo_r_cont,interpol2,color='tab:red',label=r"$\left.T(r')\right.|_{t=t_f}$")
plt.scatter(pseudo_r[:,1],T[int(10*t)],s=10,color='tab:red')


#Tiempo t = 112.74 s
t = 112.74
#Se obtiene la interpolacion
popt3, _ = curve_fit(model,pseudo_r[:,1],T[65])
#Coeficientes
a,b,c,d,e,f,g,h = popt3
interpol3 = model(pseudo_r_cont,a,b,c,d,e,f,g,h)
plt.plot(pseudo_r_cont,interpol3,color='tab:purple',label=r"$\left.T(r')\right.|_{t = 22,55\,t_f}$")
plt.scatter(pseudo_r[:,1],T[65],s=10,color='tab:purple')


#Tiempo final
t = 314.74
#Se obtiene la interpolacion
popt4, _ = curve_fit(model,pseudo_r[:,1],T[85])
#Coeficientes
a,b,c,d,e,f,g,h = popt4
interpol4 = model(pseudo_r_cont,a,b,c,d,e,f,g,h)
plt.plot(pseudo_r_cont,interpol4,color='tab:brown',label=r"$\left.T(r')\right.|_{t = 62,95\,t_f}$")
plt.scatter(pseudo_r[:,1],T[85],s=10,color='tab:brown')


plt.grid()
plt.legend()
plt.xlabel(r"$\frac{r'}{R_T}$",fontsize=13)
plt.ylabel(r"$T(r')\,\:[K]$",fontsize=13)
plt.title('Temperatura en función de la coordenada pseudo-radial')
plt.tight_layout()
plt.show()
