#23_03_10_015_Insertar-en-Listas_v1
#Eric Rodriguez Del Valle 20310419
#Practica 15 Añadir elementos usando insert.


# Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert(). 
# Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición. 
# Deberás hacer esto utilizando posiciones de lista negativas.


colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

colores.insert(-4, 'Magenta')               #Se pone a la izquierda de la posicion que le des
colores.insert(-1, 'Turquesa')
print(colores)
