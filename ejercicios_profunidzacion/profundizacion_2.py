# Bucles [Python]
# Ejercicios de profundización

# Autor: Edwin Yepez
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado
El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa
Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''
from binhex import FInfo


print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
while True:

    numero = int(input('\nIngrese el numero de opcion que desee: \n1.- SUMA (+)\n2.- RESTA (-)\n3.- MULTIPLICACION (*)\n4.- DIVISION (/)\n5.- POTENCIA (**)\n6.- FIN\n\n'))
    if numero == 6:
        break
    if numero == 1:
        numero_1 = float(input('\nIngrese el primer numero: '))
        numero_2 = float(input('\nIngrese el segundo numero: '))
        suma = numero_1 + numero_2
        print('\nEl resultado de la suma entre {} y {} es: {}'.format(numero_1,numero_2,suma))
    elif numero == 2:
        numero_1 = float(input('\nIngrese el primer numero: '))
        numero_2 = float(input('\nIngrese el segundo numero: '))
        resta = numero_1 - numero_2
        print('\nEl resultado de la resta entre {} y {} es: {}'.format(numero_1,numero_2,resta))
    elif numero == 3:
        numero_1 = float(input('\nIngrese el primer numero: '))
        numero_2 = float(input('\nIngrese el segundo numero: '))
        multiplicacion = numero_1 * numero_2
        print('\nEl resultado de la multiplicacion entre {} y {} es: {}'.format(numero_1,numero_2,multiplicacion))
    elif numero == 4:
        numero_1 = float(input('\nIngrese el primer numero: '))
        numero_2 = float(input('\nIngrese el segundo numero: '))
        division = numero_1 / numero_2
        print('\nEl resultado de la division entre {} y {} es: {}'.format(numero_1,numero_2,division))
    elif numero == 5:
        numero_1 = float(input('\nIngrese el primer numero: '))
        numero_2 = float(input('\nIngrese el segundo numero: '))
        potencia = numero_1 ** numero_2
        print('\nEl resultado de {} elevado a {} es: {}'.format(numero_1,numero_2,potencia))
    else:
        print('OPCION NO VALIDA!!')

    