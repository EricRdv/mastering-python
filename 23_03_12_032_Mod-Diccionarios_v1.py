#23_03_12_032_Mod-Diccionarios_v1
#Eric Rodriguez Del Valle 20310419
#Practica 32 Usando bucles para recorrer diccionarios


teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1                        #Eliminamos el diccionario completo
del teclado2['Categoría']           #Eliminamos solo un componente
del teclado2['Precio']

print(teclado2)                 #Imprimimos lo unico que queda del diccionario