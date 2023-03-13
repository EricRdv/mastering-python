#23_03_12_030_Diccionarios_v1
#Eric Rodriguez Del Valle 20310419
#Practica 30 Uso basico de diccionarios.

#Los diccionarios funcionan como variables con varios atributos dentro.


teclado1 = {
	'Categoría': 'Teclados',            # Nombramos cada atributo
	'Modelo': 'HyperX Alloy FPS Pro',   # Y le damos un valor
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

#Accedemos a atributos de esa manera 
print('El modelo', teclado2['Modelo'], 'cuesta', teclado2['Precio'])    

#Otra manera de imprimir todo el diccionario
print(dict(teclado2))