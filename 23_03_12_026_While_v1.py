#23_03_12_026_While_v1
#Eric Rodriguez Del Valle 20310419
#Practica 26 Introduccion a los bucles

#Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.

x = 0
while x < 15:
    x += 5          #Para aumentar en cierta cantidad
    print(x)

#Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.

x = 0
while x > -100:
    x -= 20         #Para decrementar en cierta cantidad
    print(x)

#Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1
#y que muestre en cada ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'...

x = 10
while x != 0:
    x -= 1
    print('El valor del bucle es ', x)

