#23_03_12_025_Mejorando-ifs_v1
#Eric Rodriguez Del Valle 20310419
#Practica 25 Sintaxis diferentes

x = 'Gatos'
y = 'Perro'

if x == 'Gato':
    print('Es un gato')
else:
    print('Es un perro')

#Ahora de otra manera

if x == 'Gato': print('Es un gato')
else:
    print('Es un perro')

#Una mejor

print('Es un gato') if x == 'Gato' else print('Es un perro')
