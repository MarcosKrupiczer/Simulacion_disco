#IMAGENES DE CORTES
#Grafico auxiliar para sacar la colorbar
p = pv.Plotter(window_size=(250, 600),off_screen=True)
#Objeto de la malla inicial
msh = pv.read('Malla5//disco.msh')
#Seteo de la leyenda
sargs = dict(width=0.2,height=0.8, vertical=True, position_x=0.5, position_y=0.1,title_font_size=14,label_font_size=16,font_family="courier")
#Asignacion de las temperaturas
msh.point_data['Temperatura [K]'] = Resultados[25] #t = 2.5 s
p.add_mesh(msh,scalars='Temperatura [K]',opacity=0,show_edges=False,clim=[T0,Tmax],cmap='autumn_r',scalar_bar_args=sargs)
p.show()
p.image_scale = 2
p.screenshot(f'colorbar_{Vkmh}.png')

#Objeto de la malla inicial
msh = pv.read('Malla5//disco.msh')
#Inicio del graficador
p = pv.Plotter(shape=(2, 2),window_size=(500, 700),off_screen=True)

#1er grafico
#Seteo de la camara
camera = pv.Camera()
#Posicion de camara para corte
camera.position = (-0.6, 0, 0)
camera.focal_point = (0, 0, 0)
#Asignacion de la camara
p.camera = camera
#Asignacion de las temperaturas
msh.point_data['Temperatura [K]'] = T[50] #t = 5 s (se puede elegir cualquier tiempo)
#Corte vertical
corte_vertical = msh.slice(normal=[-1, 0, 0])
#corte_vertical.translate((0, -0.025, 0), inplace=True)
#Agregado de la malla en corte
corte = p.add_mesh(corte_vertical,scalars='Temperatura [K]',show_edges=False,clim=[T0,Tmax],cmap='autumn_r',scalar_bar_args=sargs)
p.remove_scalar_bar(title=None, render=True)

#2do grafico
p.subplot(0,1)
#Seteo de la camara
camera2 = pv.Camera()
#Posicion de camara para corte
camera2.position = (-0.6, 0, 0)
camera2.focal_point = (0, 0, 0)
camera2.elevation += 90
#Asignacion de la camara
p.camera = camera2
#Asignacion de las temperaturas
msh.point_data['Temperatura [K]'] = T[50] #t = 5 s (se puede elegir cualquier tiempo)
#Corte horizontal
corte_horizontal = msh.slice([0,1,0])
corte_horizontal.translate((0, 0, -0.05), inplace=True)
#Agregado de la malla en corte
corte = p.add_mesh(corte_horizontal,scalars='Temperatura [K]',show_edges=False,clim=[T0,Tmax],cmap='autumn_r')
p.remove_scalar_bar(title=None, render=True)

#3er grafico
p.subplot(1,0)
#Seteo de la camara
camera = pv.Camera()
#Posicion de camara para corte
camera.position = (-0.6, 0, 0)
camera.focal_point = (0, 0, 0)
#Asignacion de la camara
p.camera = camera
#Asignacion de las temperaturas
msh.point_data['Temperatura [K]'] = T[-1] #t =  tf (se puede elegir cualquier tiempo)
#Corte vertical
corte_vertical = msh.slice(normal=[-1, 0, 0])
#corte_vertical.translate((0, -0.025, 0), inplace=True)
#Agregado de la malla en corte
corte = p.add_mesh(corte_vertical,scalars='Temperatura [K]',show_edges=False,clim=[T0,Tmax],cmap='autumn_r',scalar_bar_args=sargs)
p.remove_scalar_bar(title=None, render=True)

#4to grafico
p.subplot(1,1)
#Seteo de la camara
camera2 = pv.Camera()
#Posicion de camara para corte
camera2.position = (-0.6, 0, 0)
camera2.focal_point = (0, 0, 0)
camera2.elevation += 90
#Asignacion de la camara
p.camera = camera2
#Asignacion de las temperaturas
msh.point_data['Temperatura [K]'] = T[-1] #t =  tf (se puede elegir cualquier tiempo)
#Corte horizontal
corte_horizontal = msh.slice([0,1,0])
corte_horizontal.translate((0, 0, -0.05), inplace=True)
#Agregado de la malla en corte
corte = p.add_mesh(corte_horizontal,scalars='Temperatura [K]',show_edges=False,clim=[T0,Tmax],cmap='autumn_r')
p.remove_scalar_bar(title=None, render=True)

#Se muestra la imagen
p.show()
#Se escala la imagen
p.image_scale = 2
#Se guarda la imagen
p.screenshot(f'corte_{Vkmh}.png')  
