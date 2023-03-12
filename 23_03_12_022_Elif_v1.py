#23_03_12_022_Elif_v1
#Eric Rodriguez Del Valle 20310419
#Practica 22 uso de elif

# Al siguiente código añádele un par de rangos de edad. Uno de 18 años hasta 45 y otro de más de 100 años hasta 120.

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 18 and edad <=45:
    print('Tienes entre 18 y 45')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 100:
	print('Eres mayor de edad.')
elif edad >= 100 and edad <=120:
    print('Tienes entre 100 y 120')
else:
	print('Edad no válida.')

