#23_03_12_023_If-en-Strings_v1
#Eric Rodriguez Del Valle 20310419
#Practica 23 condiciones para verificar strings

colores = ("Negro", 'Blanco', 'Morado', 'Rojo')

respuesta = str(input('Ingrese el color a verificar:\n'))

if respuesta in colores:
    print('Color verificado')
else:
    print('Color inexistente')


