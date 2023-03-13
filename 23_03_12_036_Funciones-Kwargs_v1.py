#23_03_12_036_Funciones-Kwargs_v1
#Eric Rodriguez Del Valle 20310419
#Practica 36 Funciones con kwargs

# **kwargs funcionan como args pero usando tipo diccionarios 


def colores(**kwargs):
	print('El color', kwargs['color1'], 'es mi favorito.', 'El color', kwargs['color2'], 'tampoco está mal.')


colores(color1 = 'Azul', color2 = 'Morado')     #Podemos crear tantas variables como queramos.

#Me pregunto como ser utilizara pero usando tuplas o listas 
