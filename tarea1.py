'''
Instrucciones:

Escribe el codigo que le pida al usuario los siguientes 4 datos
    1) Su nombre
    2) Su apellido
    3) Un numero x
    4) Un numero y

Crea una variable saludo donde juntes un Hola con el nombre y el apellido del usuario
Crea un variable m donde multipliques los dos numeros que te dio el usuario
Crea una variable mensaje donde concatenes un texto que explica que se trata de una multiplicacion con el valor de m
Imprime el saludo y la multiplicacion en la terminal

Tips:
Recuerda que para multiplicar los numeros tienes que convertir los input a entero
Para concatenar texto con un numero entero necesitas convertirlo de vuelta a string
Para convertir un objeto a string usas la funcion "str()"
'''

# Input del usuario
nombre = input('Cual es tu nombre: ')
apellido = input('Cual es tu apellido: ')
x = int(input('Escribe el valor de x: '))
y = int(input('Escribe el valor de y: '))

# Operaciones
saludo = 'Hola ' + nombre + ' ' +  apellido
m = x * y
mensaje = 'La multiplicacion de x * y es igual a: ' + str(m)

# Impresiones
print(saludo)
print(mensaje)