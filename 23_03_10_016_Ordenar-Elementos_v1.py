#23_03_10_016_Ordenar-Elementos_v1
#Eric Rodriguez Del Valle 20310419
#Practica 16 Ordena alfabeticamente listas.


#Ordena la siguiente lista en orden alfabético descendente (de la letra 'z' a la 'a').


colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón',
          'lila', 'negro', 'rosa', 'blanco', 'naranja']

colores.sort()      #Esta funcion los ordena en orden alfabetico, de manera permanente.
colores.sort(reverse=True)          #Esta en orden alfabetico de la z - a
print(colores)

print(sorted(colores))      #Con sorted imprimimos una version en orden alfabetico. No modifica la lista.
