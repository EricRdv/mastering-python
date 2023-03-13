#23_03_12_034_Funciones-Argumentos_v1
#Eric Rodriguez Del Valle 20310419
#Practica 34 Funciones con argumentos

# *args nos permite trabajar con una cantidad indefinida de elementos 


def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')        #4
colores('lila', 'negro', 'rojo')                    #3
colores('rosa')                     #1
colores('marrón', 'naranja')        #2




def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

color_tuple = ('Azul', 'Morado', 'Verde', 'Juan')

colores(*color_tuple)       #Tenemos que poner * para que funcione.
colores('Morado', 'Rojo')   #Podemos hacer de esta manera tambien

