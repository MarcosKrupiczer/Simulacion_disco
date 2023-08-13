#VIDEOS
#Se redefine el paso temporal inicial
Δt = Δt_min #s
#Nombre del video que sera guardado
nombre = f'video_{Vkmh}.mp4'
#Objeto de la malla inicial
msh = pv.read('Malla5//disco.msh')
#Temperatura inicial de la malla
msh.point_data['Temperatura [K]'] = T[0]
#Seteo de la camara
camera = pv.Camera()
#Posicion de camara 3D
camera.position = (-0.5, 0.5, 1)
camera.focal_point = (0, 0, 0)
#Inicializacion del graficador
p = pv.Plotter()
#Apertura del modo video
p.open_movie(nombre,framerate=1/Δt)
#Asignacion de la camara
p.camera = camera
#Asignacion de la malla inicial
p.add_mesh(msh,scalars='Temperatura [K]',show_edges=True,clim=[T0,Tmax],cmap='autumn_r')
print('Orient the view, then press "q" to close window and produce movie')
#Grafico inicial (sin cerrar la ventana)
p.show(auto_close=False)
p.write_frame()
#Recorrido de los pasos temporales con rotacion del disco
for i in range(int(1+(tf-t0)/Δt_min)):
    #Definicion de la variable tiempo
    t = Δt*i
    #Asignacion del vector de temperaturas T(t=ti)
    msh.point_data['Temperatura [K]'] = T[i]
    #Eliminacion de la malla en tiempo anterior
    p.clear()
    #Rotacion de la malla en tiempo t
    rot = msh.rotate_z(ω0*t+γ*t**2/2 , inplace=False)
    #Asignacion de la malla rotada con las temperaturas actualizadas
    p.add_mesh(rot,scalars='Temperatura [K]',show_edges=True,clim=[T0,Tmax],cmap='autumn_r')
    #Se escribe el tiempo actual
    p.add_text(f't = {round(t,1)} s',font='times')
    #Actualizacion del graficador
    p.update()
    p.write_frame()

#Recorrido de los pasos temporales siguientes sin rotacion del disco
for i in range(int(1+(tf-t0)/Δt_min),len(T)):
    #Se define el paso temporal variable
    Δt = Δt_max*(1-np.exp(-(t-tf)/tf))+ Δt_min
    #Definicion de la variable tiempo
    t += Δt
    #Asignacion del vector de temperaturas T(t=ti)
    rot.point_data['Temperatura [K]'] = T[i]
    #Eliminacion de la malla en tiempo anterior
    p.clear()
    #Asignacion de la malla inicial con las temperaturas actualizadas
    p.add_mesh(rot,scalars='Temperatura [K]',show_edges=True,clim=[T0,Tmax],cmap='autumn_r')
    #Se escribe el tiempo actual
    p.add_text(f't = {round(t,1)} s',font='times')
    #Actualizacion del graficador
    p.update()
    p.write_frame()

#Cierre del graficador
p.close()
