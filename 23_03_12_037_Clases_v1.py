#23_03_12_037_Clases_v1
#Eric Rodriguez Del Valle 20310419
#Practica 37 Creacion de clases


#Similar a los diccionarios
class Usuario:          
	nombre = ''
	apellidos = ''

	def imprime_datos(self):        #Self es como si incluyera sus propios datos para trabajarlos
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario()

usuario001.nombre = 'Enrique'           #.nombre accede a ese atributo
usuario001.apellidos = 'Barros Fernández'

usuario001.imprime_datos()