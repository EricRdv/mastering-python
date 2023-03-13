#23_03_12_031_Diccionarios-Bucles_v1
#Eric Rodriguez Del Valle 20310419
#Practica 31 Usando bucles para recorrer diccionarios

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

for i in teclado1:
    print(i, '=', teclado1[i] + '.')

#Con i, obtenemos el nombre del atributo, con teclado1[i], el valor del atributo