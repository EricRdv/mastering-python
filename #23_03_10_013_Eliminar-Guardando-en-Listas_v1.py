#23_03_10_013_Eliminar-Guardando-en-Listas_v1
#Eric Rodriguez Del Valle 20310419
#Practica 13 Remover posiciones de listas.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#Colores a eliminar:        azul y blanco


del_color = colores.pop(1)                  #Eliminamos un valor y lo guardamos en la variable.
del_color = colores.pop(-2)                 #Ojo que sobreescribimos la variable

print('Colores eliminados: ' + del_color)