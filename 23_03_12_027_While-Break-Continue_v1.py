#23_03_12_027_While-Break-Continue_v1
#Eric Rodriguez Del Valle 20310419
#Practica 27 Bucles 


x = 0
while x <= 30:
    x += 1          #Para aumentar en cierta cantidad
    if x == 4 or x == 6 or x == 10:
        print('Se salto el valor: ', x , ' de x')
        continue        # Hace que se salte el resto de las acciones, continuando con el while.
    if x == 15:
        print('Se rompió la ejecución del bucle cuando x valía ', x)
        break           # Nos saca del while
    print(x)
